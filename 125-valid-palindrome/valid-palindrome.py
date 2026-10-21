class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        clean_text = re.sub(r'[^A-Za-z0-9]', '', s).lower()
        return clean_text == clean_text[::-1]