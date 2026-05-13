# GenLayer Reputation Oracle

A GenLayer Intelligent Contract that evaluates reputation claims using source text and GenLayer's non-comparative equivalence principle.

## What it does

The contract accepts:

- `profile_source`
- `claim`

Then it returns a reputation verdict:

- VERIFIED
- RISKY
- UNCLEAR

## GenLayer feature used

- `gl.eq_principle.prompt_non_comparative`

## Methods

- `evaluate_reputation(profile_source, claim)`
- `get_last_report()`

## Test

Profile source:
Bilal completed GenLayer Studio tutorials, deployed an Intelligent Contract, and submitted GitHub evidence with screenshots.

Claim:
Bilal is an active GenLayer builder.

Result:
VERIFIED

## Contract address

0x54B5a3e22C04b1A8794dE0C1Fe689459A3e050e3  
