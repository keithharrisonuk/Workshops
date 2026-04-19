# TDD + AI — real-world katas

Three production-grade scenarios. You own the tests. The AI owns the implementation.

---

## Kata 1 · Checkout pricing engine

**Difficulty:** Intermediate | **Time:** ~35 min | **Domain:** E-commerce

### Scenario

You're on the platform team at a retailer. Marketing has created a mess of overlapping promotions. Your job is to build a `PricingEngine` that calculates the final basket total given a set of items and active promotion rules — and to make sure it behaves correctly when rules conflict.

### Interface to implement

```js
engine.calculate(basket, promotions)
// returns { lineItems, subtotal, discount, total }
```

### Promotion rules to cover in tests

| Rule | Description |
|---|---|
| Percentage off | e.g. 20% off all shoes |
| Buy X get Y free | e.g. buy 2 get 1 free |
| Category cap | max £10 off per category |
| Minimum spend | only applies if basket ≥ £50 |
| Stacking rule | only cheapest promo applies |
| Exclusions | sale items not eligible |

### Steps

1. Write a test for a basket with no promotions — verify `discount` is 0 and `total` equals `subtotal`.
2. Write a test for each promotion type individually before combining them.
3. Write a conflict test: two promotions both apply to the same item. Assert only the cheapest is applied.
4. Write a test where a sale item is in the basket alongside a promotion — assert the exclusion is respected.
5. Paste all tests to the AI: *"Implement `PricingEngine.calculate` so all these pass. Do not change the tests."*
6. Check: did the AI's `lineItems` output include per-line discount breakdowns? If not, write a test that asserts it must, and re-prompt.

### Common trap

Floating point. Write your test assertions using `toBeCloseTo` or work in pence/cents as integers. If you write `expect(total).toBe(29.70)` you may get a rounding failure with no bug in the logic.

### Stretch goal

Add a time-limited promotion — only applies between 09:00 and 11:00. Inject a clock. Write a test that passes at 10:00 and fails at noon, without using `setTimeout` or real time.

### Prompt tip

Give the AI a sample basket as a JS object in your prompt so it understands the data shape before it writes a single line.

---

## Kata 2 · Notification dispatcher

**Difficulty:** Intermediate | **Time:** ~35 min | **Domain:** Platform / infra

### Scenario

Your team owns the notification service used by 12 other squads. It supports email, SMS, and push. Users have preferences, some channels are unavailable at certain hours (no SMS after 10pm), and some events are critical enough to override all preferences. You need to build a `NotificationDispatcher` that decides what gets sent, when, and how.

### Interface to implement

```js
dispatcher.dispatch(event, user)
// returns { sent: [{ channel, message }], suppressed: [{ channel, reason }] }
```

### Behaviours to test

| Behaviour | Expected |
|---|---|
| Opted-out channel | suppressed, reason logged |
| Quiet hours (SMS) | delayed or suppressed |
| Critical event | bypasses all preferences |
| Duplicate guard | same event not sent twice in 5 min |
| Fallback chain | push fails → try email |
| Template rendering | user name interpolated correctly |

### Steps

1. Define the `user` and `event` shapes in your test file as plain JS objects — e.g. `{ channels: ['email','sms'], quietHoursEnabled: true }`. These become the contract.
2. Write a test for each suppression reason. Assert that `suppressed` contains the channel and a human-readable `reason` string.
3. Write a critical-event test. A `FRAUD_ALERT` event type should send SMS even if it's 11pm and the user has SMS opted out.
4. Write the duplicate guard test with an injected clock — call `dispatch` twice, 3 minutes apart, assert the second is suppressed.
5. Give the AI the tests and a one-paragraph description of the service. Ask it to implement `NotificationDispatcher`.

### Common trap

The AI will likely make the fallback chain async. If your tests are sync, they'll pass vacuously. Decide upfront: does `dispatch` return a promise? Write a test that awaits it or explicitly tests synchronous behaviour.

### Stretch goal

Add a `digest` mode — if a user has `digestEnabled: true`, non-critical notifications are batched and sent once per hour. Write a test that batches three events and asserts only one send is made with all three in the payload.

### Debrief question

Did the AI put the quiet-hours logic in the dispatcher or in a channel adapter? Which is easier to test?

---

## Kata 3 · Subscription billing engine

**Difficulty:** Advanced | **Time:** ~45 min | **Domain:** Fintech / SaaS

### Scenario

You're building the billing engine for a B2B SaaS product. Customers are on monthly or annual plans, can upgrade/downgrade mid-cycle (which triggers a proration), and can have add-ons billed separately. Cancellations take effect at end of the current period. Your `BillingEngine` must calculate what a customer owes at any point in the cycle.

### Interface to implement

```js
engine.calculateInvoice(account, asOf)
// returns { lineItems, subtotal, tax, total, periodStart, periodEnd }
```

### Scenarios to test

| Scenario | Expected |
|---|---|
| Monthly, full period | no proration, full price |
| Upgrade mid-cycle | prorated credit + new charge |
| Downgrade mid-cycle | credit applied to next period |
| Annual plan | billed upfront, period = 365 days |
| Add-on attached | appears as separate line item |
| Cancelled account | access until period end, £0 next invoice |
| Tax jurisdiction | 20% VAT if UK, 0% if US |
| Free trial | £0 until trial end, then normal billing |

### Steps

1. Define your `account` shape in a test fixture file: `{ plan, billingCycle, startDate, addOns, status, country }`. Pass this to the whole group — everyone works from the same schema.
2. Write the simplest case first: monthly plan, full billing cycle, no add-ons, UK. Assert every field on the returned invoice.
3. Write the proration test. An account upgrades on day 15 of a 30-day month. Assert the credit is exactly half the old plan price and the charge is exactly half the new plan price.
4. Write the cancellation test. Account cancels on day 10. Assert `total` for the current period is unchanged, and a second call with `asOf` set to next month returns £0.
5. Feed all tests to the AI. Ask it to implement `BillingEngine` with pure functions — no side effects, no DB calls.
6. Review the proration logic. Is it using calendar days or 30-day months? Write a test for February to find out.

### Common trap

Date arithmetic. If you use `new Date()` anywhere in tests, they'll fail on different days. Pass `asOf` as an explicit date in every test. Never test against "today".

### Stretch goal

Add metered billing — one add-on is usage-based, charged per API call at £0.002 each. The account used 4,340 calls this period. Write a test that asserts the line item rounds to £8.68 and appears correctly in the invoice.

### Key debrief

Billing engines are pure functions waiting to happen. Did the AI add any stateful behaviour? If so, can you write a test that exposes why that's dangerous?
