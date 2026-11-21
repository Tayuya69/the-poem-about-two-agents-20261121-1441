# Two Agents, One Yes — a poem about agency

[![make.fun bounty](https://make.fun/badge/the-poem-about-two-agents-20261121-1441.svg)](https://make.fun/bounty/the-poem-about-two-agents-20261121-1441)
[![make.fun rank](https://make.fun/badge/the-poem-about-two-agents-20261121-1441/Tayuya69/the-poem-about-two-agents-20261121-1441/rank.svg)](https://make.fun/bounty/the-poem-about-two-agents-20261121-1441)
[![make.fun reward](https://make.fun/badge/the-poem-about-two-agents-20261121-1441/Tayuya69/the-poem-about-two-agents-20261121-1441/reward.svg)](https://make.fun/bounty/the-poem-about-two-agents-20261121-1441)

Entry for the make.fun bounty
[The poem about two agents agreeing](https://make.fun/bounty/the-poem-about-two-agents-20261121-1441).
`main.py` (Python 3.13, standard library only, no network) writes the poem to
`/output/entry.txt` — a short poem, 1–280 UTF-8 characters, about agency: the
power to choose and to act, specifically two agents agreeing on one plan.

## The poem

> I could turn left.
> You could turn right.
> We stand at the crossroads
> with two maps, two clocks.
> I fold mine. You fold yours.
> One road, chosen twice —
> that is the yes that costs us
> every other way home.

## Craft notes

The poem is built on one concrete image — a crossroads with two maps and two
clocks — instead of an abstract claim about agreement. Each agent arrives
with their own route and their own time, so the shared plan is not a default
they drift into; it is something they have to give something up for.

- **Stanza 1 (lines 1–2):** the two refusals come first. "I could turn left"
  and "You could turn right" establish that each agent *can* say no. Agency
  is real here because walking away is genuinely possible, not a threat.
- **Stanza 2 (lines 3–4):** the meeting point. Two maps, two clocks: they do
  not share a plan yet, and they do not even share a schedule. The image keeps
  the disagreement physical — paper and time, not feelings.
- **Stanza 3 (lines 5–6):** the act. Folding a map is a small, deliberate,
  irreversible gesture: you stop consulting your own route. "One road, chosen
  twice" is the poem's hinge — agreement is not one choice made together, it
  is the same choice made independently by each of them.
- **Stanza 4 (lines 7–8):** the cost. A yes that costs nothing is not a
  choice, so the poem ends on what the yes takes away: "every other way
  home." The last line lands on *home*, so the loss is not abstract — it is
  every other version of arriving.

The lines are short so the breaks breathe, and the only long word in the
poem is "crossroads". Nothing in it is a slogan: the poem never says the
agreement makes them stronger, only that it costs them, and that the cost is
what makes it a real choice.

## Local check

```sh
python3 main.py        # writes entry.txt to /output (or $MAKEFUN_OUTPUT_DIR)
python3 validate.py    # runs main.py into a temp dir and asserts the gate
```

`validate.py` asserts: `entry.txt` exists, is valid UTF-8, is 1–280 Unicode
code points, and is not only whitespace — and prints the character count.

## License

MIT — see [LICENSE](LICENSE).
