
class Solution
  def twoSum(nums, target)
    arr = []
    for i in (0 .. (nums.count - 1)) do
      p nums.count
      for j in ((i.to_i + 1)..(nums.count - 2)) do
        break arr = [i, j] if nums[i] + nums[j] == target
      end
    end
    arr
  end
end
p Solution.new.twoSum([4,5,6], 10)

# Output: [0,1]
# ========================================
class Solution
  def isAnagram(s, t)
    t_chars = t.chars
    s.chars.each do |char|
      break false if !t_chars.index(char)
      t_chars.delete_at(t_chars.index(char))
    end
    t_chars.empty?
  end
end

p Solution.new.isAnagram("racecar","carrace")
# ========================================
class Solution
  def hasDuplicate(nums)
    h = {}
    nums.each do |num|
      h[num] = h[num] ? h[num] + 1 : 1
      break true if h[num] > 1
    end
    false
  end
end

nums = [1,2,3,4]
p Solution.new.hasDuplicate(nums)
# ========================================