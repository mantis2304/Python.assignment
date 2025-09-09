
# 1. Print all numbers between 1 and 500 divisible by 3 and sum of digits > 10
print("Q1: Numbers divisible by 3 with digit sum > 10")
for num in range(1, 501):
    if num % 3 == 0:
        digit_sum = sum(int(d) for d in str(num))
        if digit_sum > 10:
            print(num, end=" ")
print("\n")

# 2. Find all Armstrong numbers between 1 and 10,000
print("Q2: Armstrong Numbers between 1 and 10000")
for num in range(1, 10001):
    power = len(str(num))
    total = sum(int(d)**power for d in str(num))
    if num == total:
        print(num, end=" ")
print("\n")

# 3. Print all prime numbers between 1 and N, skip numbers ending with 3
print("Q3: Prime numbers up to N (excluding those ending with 3)")
N = 100
for num in range(2, N+1):
    if str(num).endswith("3"):
        continue
    is_prime = True
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num, end=" ")
print("\n")

# 4. Reverse a number without slicing using while loop
print("Q4: Reverse a number using while loop")
num = 12345
reverse = 0
temp = num
while temp > 0:
    digit = temp % 10
    reverse = reverse * 10 + digit
    temp //= 10
print("Original:", num, "Reversed:", reverse)
print()

# 5. Print first N Fibonacci numbers using loops
print("Q5: First N Fibonacci numbers")
N = 10
a, b = 0, 1
print(a, b, end=" ")
for _ in range(2, N):
    c = a + b
    print(c, end=" ")
    a, b = b, c
print("\n")

# ======================
# Pattern Making
# ======================

# 6. Pyramid pattern for N=5
print("Q6: Pyramid Pattern")
N = 5
for i in range(1, N+1):
    num = i
    # left spaces
    print(" "*(N-i), end="")
    # increasing numbers
    for j in range(i):
        print(num, end="")
        num += 1
    # decreasing numbers
    num -= 2
    for j in range(i-1):
        print(num, end="")
        num -= 1
    print()

# 7. Spiral matrix of size NxN
print("\nQ7: Spiral Matrix")
N = 4
matrix = [[0]*N for _ in range(N)]
top, left, right, bottom = 0, 0, N-1, N-1
val = 1
while left <= right and top <= bottom:
    for i in range(left, right+1):
        matrix[top][i] = val
        val += 1
    top += 1
    for i in range(top, bottom+1):
        matrix[i][right] = val
        val += 1
    right -= 1
    for i in range(right, left-1, -1):
        matrix[bottom][i] = val
        val += 1
    bottom -= 1
    for i in range(bottom, top-1, -1):
        matrix[i][left] = val
        val += 1
    left += 1
for row in matrix:
    print(row)

# 8. Diamond pattern of '*' with odd rows
print("\nQ8: Diamond Pattern")
N = 5
for i in range(1, N+1, 2):
    print(" " * ((N-i)//2) + "*"*i)
for i in range(N-2, 0, -2):
    print(" " * ((N-i)//2) + "*"*i)

# 9. Pascal's Triangle up to N rows
print("\nQ9: Pascal's Triangle")
N = 5
for i in range(N):
    val = 1
    print(" "*(N-i), end="")
    for j in range(i+1):
        print(val, end=" ")
        val = val * (i-j)//(j+1) if j < i else 1
    print()

# 10. Alphabet triangle
print("\nQ10: Alphabet Triangle")
N = 5
for i in range(1, N+1):
    for j in range(i):
        print(chr(65+j), end="")
    print()

# 11. Grade based on marks
print("\nQ11: Grade using match-case")
marks = 85
match marks//10:
    case 10 | 9:
        grade = "A"
    case 8:
        grade = "B"
    case 7:
        grade = "C"
    case 6:
        grade = "D"
    case _:
        grade = "F"
print("Marks:", marks, "Grade:", grade)

# 12. FizzBuzz problem
print("\nQ12: FizzBuzz")
for num in range(1, 21):
    if num % 35 == 0:
        print("FizzBuzz", end=" ")
    elif num % 5 == 0:
        print("Fizz", end=" ")
    elif num % 7 == 0:
        print("Buzz", end=" ")
    else:
        print(num, end=" ")
print()

# 13. Calculator using match-case
print("\nQ13: Calculator")
a, b, op = 10, 5, "+"
match op:
    case "+":
        print("Sum:", a+b)
    case "-":
        print("Difference:", a-b)
    case "*":
        print("Product:", a*b)
    case "/":
        print("Division:", a/b if b != 0 else "Error: Divide by zero")

# 14. Leap year check
print("\nQ14: Leap Year Check")
year = 2024
if (year % 400 == 0) or (year % 100 != 0 and year % 4 == 0):
    print(year, "is a leap year")
else:
    print(year, "is not a leap year")

# 15. Identify character type
print("\nQ15: Character Identification")
ch = "A"
if ch.isdigit():
    print("Digit")
elif ch.isalpha():
    if ch.lower() in "aeiou":
        print("Vowel")
    else:
        print("Consonant")
else:
    print("Special Character")


# 16. GCD and LCM of two numbers
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a*b // gcd(a, b)

print("\nQ16: GCD and LCM")
print("GCD:", gcd(12, 18))
print("LCM:", lcm(12, 18))

# 17. Second largest element without sorted()
print("\nQ17: Second Largest in List")
arr = [10, 20, 4, 45, 99]
first = second = float('-inf')
for num in arr:
    if num > first:
        second = first
        first = num
    elif num > second and num != first:
        second = num
print("Second Largest:", second)

# 18. Palindrome check (ignore case and spaces)
print("\nQ18: Palindrome Check")
s = "Race car"
clean = "".join(ch.lower() for ch in s if ch.isalnum())
print("Palindrome" if clean == clean[::-1] else "Not Palindrome")

# 19. Multiplication table up to N
print("\nQ19: Multiplication Table")
N = 5
for i in range(1, N+1):
    for j in range(1, 11):
        print(f"{i} x {j} = {i*j}")
    print()

# 20. Recursive sum of digits
print("\nQ20: Recursive Sum of Digits")
def sum_digits(n):
    if n == 0:
        return 0
    return n % 10 + sum_digits(n//10)
print("Sum of digits:", sum_digits(1234))

# 21. All permutations of a string (without itertools)
print("\nQ21: String Permutations")
def permute(s, chosen=""):
    if not s:
        print(chosen)
    else:
        for i in range(len(s)):
            permute(s[:i]+s[i+1:], chosen+s[i])
permute("ABC")

# 22. Longest palindrome substring (simple approach)
print("\nQ22: Longest Palindrome Substring")
s = "babad"
longest = ""
for i in range(len(s)):
    for j in range(i+1, len(s)+1):
        sub = s[i:j]
        if sub == sub[::-1] and len(sub) > len(longest):
            longest = sub
print("Longest Palindrome:", longest)

# 23. Word frequency ignoring case
print("\nQ23: Word Frequency")
text = "This is a test this IS only a Test"
words = text.lower().split()
freq = {}
for w in words:
    freq[w] = freq.get(w, 0) + 1
print(freq)

# 24. Check anagrams without Counter
print("\nQ24: Anagram Check")
s1, s2 = "listen", "silent"
print("Anagrams" if sorted(s1) == sorted(s2) else "Not Anagrams")

# 25. Remove duplicate characters preserving order
print("\nQ25: Remove Duplicates")
s = "programming"
result = ""
for ch in s:
    if ch not in result:
        result += ch
print(result)

# 26. Rotate list k times to right without slicing
print("\nQ26: Rotate List")
arr = [1,2,3,4,5]
k = 2
for _ in range(k):
    last = arr.pop()
    arr.insert(0, last)
print(arr)

# 27. Merge two sorted lists without sorted()
print("\nQ27: Merge Sorted Lists")
a = [1,3,5]
b = [2,4,6]
merged = []
i=j=0
while i < len(a) and j < len(b):
    if a[i] < b[j]:
        merged.append(a[i]); i+=1
    else:
        merged.append(b[j]); j+=1
merged.extend(a[i:])
merged.extend(b[j:])
print(merged)

# 28. Longest increasing subsequence (simple O(n^2) solution)
print("\nQ28: Longest Increasing Subsequence")
arr = [10,22,9,33,21,50,41,60]
dp = [1]*len(arr)
for i in range(len(arr)):
    for j in range(i):
        if arr[i] > arr[j]:
            dp[i] = max(dp[i], dp[j]+1)
print("Length:", max(dp))

# 29. Find pairs with given sum
print("\nQ29: Pairs with sum target")
arr = [2,4,3,5,7,8,9]
target = 7
pairs = []
for i in range(len(arr)):
    for j in range(i+1, len(arr)):
        if arr[i]+arr[j] == target:
            pairs.append((arr[i], arr[j]))
print(pairs)

# 30. Remove None and duplicates
print("\nQ30: Remove None and Duplicates")
arr = [1, None, 2, 2, None, 3, 3, 4]
clean = []
for i in arr:
    if i is not None and i not in clean:
        clean.append(i)
print(clean)

# 31. Swap two tuples without extra variable
print("\nQ31: Swap Tuples")
a, b = (1,2), (3,4)
a, b = b, a
print(a,b)

# 32. Element-wise sum of tuples
print("\nQ32: Element-wise Sum")
a, b = (1,2,3), (4,5,6)
print(tuple(x+y for x,y in zip(a,b)))

# 33. Convert list of tuples to dictionary
print("\nQ33: List of Tuples to Dict")
lst = [("a",1), ("b",2)]
print(dict(lst))

# 34. Count repeated elements in tuple
print("\nQ34: Count Repeated")
t = (1,2,2,3,4,4,4)
freq = {}
for i in t:
    freq[i] = freq.get(i,0)+1
print(freq)

# 35. Swap min and max elements in tuple
print("\nQ35: Swap Min and Max")
t = (3,1,4,2)
lst = list(t)
min_i, max_i = lst.index(min(lst)), lst.index(max(lst))
lst[min_i], lst[max_i] = lst[max_i], lst[min_i]
print(tuple(lst))

# 36. Elements in exactly two out of three sets
print("\nQ36: Elements in exactly two sets")
A,B,C = {1,2,3},{2,3,4},{3,4,5}
res = (A&B) | (B&C) | (A&C)
res -= (A&B&C)
print(res)

# 37. Check if sets are disjoint without isdisjoint()
print("\nQ37: Disjoint Sets Check")
A,B = {1,2,3},{4,5}
print("Disjoint" if not (A & B) else "Not Disjoint")

# 38. Symmetric difference manually
print("\nQ38: Symmetric Difference")
A,B = {1,2,3},{3,4,5}
print((A-B)|(B-A))

# 39. Unique vowels in a string
print("\nQ39: Unique Vowels in String")
s = "Hello World"
print({ch for ch in s.lower() if ch in "aeiou"})

# 40. Prime factors as set
print("\nQ40: Prime Factors")
num = 28
factors = set()
for i in range(2,num+1):
    while num % i == 0:
        factors.add(i)
        num//=i
print(factors)

# 41. Frequency of characters in string
print("\nQ41: Character Frequency")
s = "programming"
freq = {}
for ch in s:
    freq[ch] = freq.get(ch,0)+1
print(freq)

# 42. Merge dictionaries and sum values
print("\nQ42: Merge Dictionaries")
d1, d2 = {"a":1,"b":2}, {"b":3,"c":4}
merged = d1.copy()
for k,v in d2.items():
    merged[k] = merged.get(k,0)+v
print(merged)

# 43. Invert dictionary
print("\nQ43: Invert Dictionary")
d = {"a":1,"b":2}
print({v:k for k,v in d.items()})

# 44. Group words by first letter
print("\nQ44: Group Words by First Letter")
words = ["apple","banana","apricot","cherry"]
grouped = {}
for w in words:
    grouped.setdefault(w[0], []).append(w)
print(grouped)

# 45. Key with highest value
print("\nQ45: Key with Highest Value")
d = {"a":10,"b":20,"c":5}
print(max(d,key=d.get))
