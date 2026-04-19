# TDD + AI kata · Password validator

**Difficulty:** Beginner | **Time:** ~20 min | **Domain:** Auth / validation

---

## Scenario

You're adding a password strength requirement to a user registration flow. Your job is to write the tests that define what a valid password looks like. The AI's job is to make them all pass.

## Interface to implement

```js
isValidPassword(password)
// returns true or false
```

## Rules to test

| Rule | Requirement |
|---|---|
| Minimum length | 8 characters |
| Uppercase | at least 1 uppercase letter |
| Number | at least 1 digit |
| Special character | at least one of: `! @ # $ % ^` |

## Steps

1. Write a failing test for each rule above — one test per rule.
2. Add edge cases: empty string, whitespace only, exactly 8 characters, exactly 7 characters.
3. Write a test for a password that satisfies every rule — assert it returns `true`.
4. Paste your tests into the AI: *"Implement `isValidPassword` so all these tests pass. Do not modify the tests."*
5. Run the tests. If any fail, describe the failure to the AI — don't edit the implementation yourself.

## Example test structure (Jest)

```js
describe('isValidPassword', () => {
  it('returns false for passwords shorter than 8 characters', () => {
    expect(isValidPassword('Ab1!')).toBe(false)
  })

  it('returns false when no uppercase letter is present', () => {
    expect(isValidPassword('abcdef1!')).toBe(false)
  })

  // your tests go here...
})
```

## Common trap

It's tempting to write one big test with a valid password and call it done. Resist. If you only test the happy path, the AI can pass your tests with `return true`. Each rule needs its own failing case.

## Stretch goal

Add a test for common passwords — `"Password1!"` should be rejected even though it passes all four rules. Can you make the AI add a blocklist without touching the existing tests?

## Debrief question

What happens if you give the AI your tests with no other context — no function name, no description? Does it infer the contract correctly from the tests alone?
