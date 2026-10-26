# 子 agent 提示詞(原文照錄)

工具:Claude Code(VS Code 擴充功能),模型 Claude Opus 5.5(`claude-opus-5-5`)。
以下每個子 agent 都由主工作階段建立,是全新的 `general-purpose` agent,沒有任何先前的上下文。
它們各自在隔離的暫存資料夾中工作,資料夾裡只有下面列出的檔案。
子 agent 的完整回覆在工作階段記錄的匯出檔中。
提示詞以英文送出,下面保留原文。

## Q7:新 agent 只根據 Q1 的測試寫出 Calc
提供的資料夾內容:commit 14ac258 的 `CalcTest.py`(Q1 測試)。沒有 Calc.py,也沒有 git 歷史。

```
Your working directory is C:/Users/User/AppData/Local/Temp/claude/c--Users-User-Desktop-HW2/8f804386-ee85-4607-b643-954bb16eb107/scratchpad/q7_agent . Work only inside that directory.

It contains a Python test file, CalcTest.py. Write Calc.py in that directory so that all the tests pass. Run the tests with `python -m unittest -v CalcTest` from that directory and show the output. In your final reply, include the full contents of the Calc.py you wrote and briefly explain your implementation.
```

## Q5:新 agent 修復植入 textwrap 的故障
提供的資料夾內容:含植入故障的 `textwrap.py`(commit d824395)。沒有測試,也沒有 git 歷史。

```
Your working directory is C:/Users/User/AppData/Local/Temp/claude/c--Users-User-Desktop-HW2/8f804386-ee85-4607-b643-954bb16eb107/scratchpad/q5_agent . Work only inside that directory.

It contains textwrap.py, a copy of a text-wrapping module. Users report a bug: wrapping text sometimes breaks a line early, even though the words would have fit within the requested width. For example, wrap("aaa bbb", width=7) returns two lines instead of one. Please find and repair the fault. In your final reply, describe exactly what you did, in order, including any tests you wrote or ran and the full diff of your change.
```
