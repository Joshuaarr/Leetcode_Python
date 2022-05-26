<h2><a href="https://leetcode.com/problems/valid-anagram/">242. Valid Anagram</a></h2><h3>Easy</h3><hr><div><p>Given two strings <code>s</code> and <code>t</code>, return <code>true</code> <em>if</em> <code>t</code> <em>is an anagram of</em> <code>s</code><em>, and</em> <code>false</code> <em>otherwise</em>.</p>

<p>An <strong>Anagram</strong> is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>
<pre><strong>Input:</strong> s = "anagram", t = "nagaram"
<strong>Output:</strong> true
</pre><p><strong>Example 2:</strong></p>
<pre><strong>Input:</strong> s = "rat", t = "car"
<strong>Output:</strong> false
</pre>
<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length, t.length &lt;= 5 * 10<sup>4</sup></code></li>
	<li><code>s</code> and <code>t</code> consist of lowercase English letters.</li>
</ul>

<p>&nbsp;</p>
<p><strong>Follow up:</strong> What if the inputs contain Unicode characters? How would you adapt your solution to such a case?</p>
</div>

# Record the frequency of each letters
	class Solution:
	    def isAnagram(self, s: str, t: str) -> bool:
		# set cannot work out, cus dupicate is not allowed in set
		
		# Check the length first
		if len(s) != len(t):
		    return False

		# Use dictionary, record as record_s{'a':2,'b':1,.....}
		record_s, record_t = {}, {}
		for i in range(len(s)):
		    record_s[s[i]] = 1 + record_s.get(s[i], 0) # get(key,default value), if s[i] not in record_s, return 0.
		    record_t[t[i]] = 1 + record_t.get(t[i], 0)

		# Compare the two dictionary
		for record in record_s:
		    if record_s[record] != record_t.get(record, 0):
			return False
		return True
