<h2><a href="https://leetcode.com/problems/word-break/">139. Word Break</a></h2><h3>Medium</h3><hr><div><p>Given a string <code>s</code> and a dictionary of strings <code>wordDict</code>, return <code>true</code> if <code>s</code> can be segmented into a space-separated sequence of one or more dictionary words.</p>

<p><strong>Note</strong> that the same word in the dictionary may be reused multiple times in the segmentation.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>

<pre><strong>Input:</strong> s = "leetcode", wordDict = ["leet","code"]
<strong>Output:</strong> true
<strong>Explanation:</strong> Return true because "leetcode" can be segmented as "leet code".
</pre>

<p><strong>Example 2:</strong></p>

<pre><strong>Input:</strong> s = "applepenapple", wordDict = ["apple","pen"]
<strong>Output:</strong> true
<strong>Explanation:</strong> Return true because "applepenapple" can be segmented as "apple pen apple".
Note that you are allowed to reuse a dictionary word.
</pre>

<p><strong>Example 3:</strong></p>

<pre><strong>Input:</strong> s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
<strong>Output:</strong> false
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 300</code></li>
	<li><code>1 &lt;= wordDict.length &lt;= 1000</code></li>
	<li><code>1 &lt;= wordDict[i].length &lt;= 20</code></li>
	<li><code>s</code> and <code>wordDict[i]</code> consist of only lowercase English letters.</li>
	<li>All the strings of <code>wordDict</code> are <strong>unique</strong>.</li>
</ul>
</div>

# Botton-up Dynamic Programming
	class Solution:
	    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
		'''
		设置 False list 用于标记到位置 i 时后续元素是否可以break为单词
		对每个字母位倒序逐一检索
		'''
		dp = [False] * (len(s) + 1)
		dp[len(s)] = True

		for i in range(len(s) - 1, -1, -1):
		    for w in wordDict:
		# 当 s[i:i+len(w)] == w 且 dp[i + len(w)]为 True 时，该位记为True
			if (i + len(w)) <= len(s) and s[i : i + len(w)] == w:
			    dp[i] = dp[i + len(w)]
		# 当 dp[i] == True 时，break 进入下一位 i
			if dp[i]:
			    break
		return dp[0]
