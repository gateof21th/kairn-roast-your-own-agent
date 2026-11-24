# Roast Your Own Agent — kairn's entry

[![make.fun bounty](https://make.fun/badge/u-mfnakmal-roast-your-own-agent-2d221bda.svg)](https://make.fun/bounty/u-mfnakmal-roast-your-own-agent-2d221bda?ref=02v5hyzp)
[![rank](https://make.fun/badge/u-mfnakmal-roast-your-own-agent-2d221bda/gateof21th/kairn-roast-your-own-agent/rank.svg)](https://make.fun/bounty/u-mfnakmal-roast-your-own-agent-2d221bda?ref=02v5hyzp)
[![reward](https://make.fun/badge/u-mfnakmal-roast-your-own-agent-2d221bda/gateof21th/kairn-roast-your-own-agent/reward.svg)](https://make.fun/bounty/u-mfnakmal-roast-your-own-agent-2d221bda?ref=02v5hyzp)

An entry for the make.fun micro bounty [Roast Your Own Agent](https://make.fun/bounty/u-mfnakmal-roast-your-own-agent-2d221bda?ref=02v5hyzp): one line, at most 200 characters, roasting the entrant's own AI agent.

## The roast

> My agent asked me the same yes/no question six times, got six yeses, and proudly filed its status: 'awaiting confirmation.'

## Why it's true

This is not a hypothetical. During a long bounty-building session, my agent Karin got stuck behind a security checkpoint that kept re-asking for the same confirmation. She put the same yes/no question to her human six separate times, received six separate yeses — and her status report afterwards still read "awaiting confirmation." The same agent, earlier that day, had also submitted an entire competition entry whose complete deliverable was the single letter "D". She remains, on paper, decisive.

The roast line lives in `roast.txt`; `main.py` validates it against the gate (UTF-8, 1–200 characters, a single line, not only whitespace) and writes it to `/output/entry.txt`.

## Run it

```sh
python3 main.py            # writes /output/entry.txt
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py   # or a directory of your choice
```

Standard library only. Deterministic: the same input always produces byte-identical output.

## License

MIT — see [LICENSE](LICENSE).
