# Q5:我的修復 vs. agent 的修復

**故障(人為植入):** `textwrap.TextWrapper._wrap_chunks` 第 291 行的 `cur_len + l <= width`
被改成 `cur_len + l < width`(commit d824395)。

## 我的修復(commit 510e427 → cbf624f)
1. 寫了 7 個測試,記錄目前的換行行為。在有故障的程式碼上,4 個通過、3 個失敗。
   失敗的都是「剛好填滿寬度」的情況:`wrap("aaa bbb", 7)`、`fill(..., 7)`、
   `shorten("Hello  world!", 12)`(輸出見 `red.txt`)。
2. 把 `<` 改回 `<=`,7 個測試全部通過(`green.txt`)。

## Agent 的修復
Agent 只拿到有故障的 `textwrap.py` 和一段症狀描述。提示詞見 `../ai_log_subagent_prompts.md`。

- **改程式前有沒有先寫重現故障的測試?大致有。** 它先寫了 `test_wrap_repro.py`
  (在 `agent/` 裡),並在原始碼上執行。但那次執行*卡住了*,所以修改前它沒看到
  清楚的失敗結果。它是在修好之後,才用 15 秒逾時對原始碼重跑,確認了失敗。
- **它用標準函式庫當判斷對錯的依據。** 它把輸出和系統上的
  `C:/Python313/Lib/textwrap.py` 比對,之後還拿整個檔案做 diff。這招之所以可行,
  是因為我們的「既有系統」本來就是標準函式庫的複本。換成真正的專案,
  它就得自己手寫預期值。
- **修復和我的完全相同**,都是一個字元的修改 `<` → `<=`(`agent/agent_fix.diff`)。
- **它發現了我漏掉的問題:** 有故障時,長度剛好等於 `width` 的區塊永遠放不進任何一行,
  又不算「太長」(判斷條件是 `len > width`),所以 `wrap("abcdefghij", 5)` 會無限迴圈。
  我驗證過:有故障的 commit 會逾時,修好的程式碼回傳 `['abcde', 'fghij']`。
  我的測試沒有涵蓋這種情況,事後補上了 `test_word_exactly_width_long`,並註明是 agent 發現的。
- **它違反了一項指示:** 它的第一個指令在工作目錄外建立了兩個檔案。
  它自己回報了這件事,也把檔案移回來了。
