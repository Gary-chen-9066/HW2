# Q5: my repair vs. the agent's repair

**Fault (seeded):** `textwrap.TextWrapper._wrap_chunks`, line 291, `cur_len + l <= width`
was changed to `cur_len + l < width` (commit d824395).

## My repair (commits 510e427 → cbf624f)
1. I wrote 7 tests that capture the current wrap behavior. 4 pass on the faulty code. 3 fail:
   the exact-fit cases `wrap("aaa bbb", 7)`, `fill(..., 7)`, and `shorten("Hello  world!", 12)`
   (output: `red.txt`).
2. I changed `<` back to `<=`, and all 7 tests pass (`green.txt`).

## Agent's repair
The agent was given only the faulty `textwrap.py` and a symptom report. Prompt: `../ai_log_subagent_prompts.md`.

- **Did it write a reproducing test before changing the code? Mostly yes.** It wrote
  `test_wrap_repro.py` (in `agent/`) first and ran it on the original. That run *hung*, so it
  never saw a clean red result before fixing the code. It confirmed the failures against
  the original only after the fix, using a 15-second timeout.
- **Its test oracle was the stdlib.** It compared the output with the system's
  `C:/Python313/Lib/textwrap.py` and later diffed the whole file against it. That only works
  because the "existing system" is a copy of the stdlib. With a real project it would have
  needed hand-written expected values.
- **The repair is identical to mine**, a one-character change `<` → `<=` (`agent/agent_fix.diff`).
- **It found something I missed:** with the fault, a chunk exactly `width` long never fits
  on a line. It also isn't "too long" (`len > width`), so `wrap("abcdefghij", 5)` loops forever.
  I verified this: the faulty commit times out, and the fixed code returns `['abcde', 'fghij']`. My suite had
  no case for this. I added `test_word_exactly_width_long` afterwards, credited to the agent.
- **It broke an instruction:** its first command wrote two files outside its working
  directory. It reported this itself and moved them back.
