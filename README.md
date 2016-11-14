#Kaufland Interview Exercise
There are two solutions
##For Solution_1

#### 1. Create a list named words and save all word in words.
```java
List<String> words = new ArrayList<String>();
```
**words**

| index |0|1| 2|3|4|5|6|
|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|
| word | act | cat |tree | race | care | acre | bee |

####2. Create a list named anagrams.
```java
List<Word> anagrams = new ArrayList<Word>();
```
Sort individual word and save each word in anagrams List
```java
for (int i = 0; i < words.size(); i++) {
			String anagram = words.get(i);
			char[] cArr = anagram.toCharArray();
			Arrays.sort(cArr);
			anagram = String.valueOf(cArr);
			Word w = new Word(i, anagram);
			anagrams.add(w);
}
```
**anagrams**
 
| index |0|1| 2|3|4|5|6|
|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|
| position |0|1| 2|3|4|5|6|
| anagram | act | act |eert | acer | acer | acer | bee |

####3. Sort the anagrams array.
```java
public int compareTo(Object obj) {
		Word wordobj = (Word) obj;
		// if length is different, short one should be front
		if (this.word.length() != wordobj.getWord().length()) {
			return this.word.length() - wordobj.getWord().length();
		} else {
			// if length is same, lexicographic order
			return this.word.compareTo(wordobj.getWord());
		}
	}
```
**anagrams**
 
| index |0|1| 2|3|4|5|6|
|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|
| position |0|1| 6|3|4|5|2|
| anagram | act | act |bee | acer | acer | acer | eert |

####4. Output result
```java
for (int i = 0; i < anagrams.size();) {
			List<Word> result = new ArrayList<Word>();
			result.add(anagrams.get(i));
			int j;
			// find the anagrams and save in result
			for (j = i + 1; j < anagrams.size(); j++) {
				if (anagrams.get(i).getWord().equals(anagrams.get(j).getWord())) {
					result.add(anagrams.get(j));
				} else {
					break;
				}
			}
			i = j;
			if (result.size() > 1) {
				List<String> resultString = new ArrayList<String>();
				for (Word w : result) {
					resultString.add(words.get(w.getPosition()));
				}
				// Sort the result for output
				Collections.sort(resultString);
				for (j = 0; j < resultString.size() - 1; j++) {
					out.write(resultString.get(j) + " ");
				}
				// Last one should output \n
				out.write(resultString.get(j) + "\n");
			}
		}
		out.flush();
		// close the output
		out.close();
```
According to position find the original word.
Output in output.txt.

##How will your application cope with larger datasets, say 10 Million Words, and 100 Billion Words? If you wanted to cover these cases, how would you scale your application?

We using modularized program.
**If words length is different, they cannot be anagrams.**

##For Solution_2

#### 1. Create a list named wordsList
```java
LinkedList<LinkedList<String>> wordsList = new LinkedList<LinkedList<String>>();
```
**According to word length save each word in different sublist.**

**wordsList**
List 0
words length is 1
Null

List 1
words length is 2
Null

List 2
words length is 3

| index | 0   | 1    | 2   |
|:-----:|:---:|:----:|:---:|
| word  | act | cat  | bee |

List 3
words length is 4

| index | 0   | 1    | 2   | 3    |
|:-----:|:---:|:----:|:---:|:----:|
| word  | tree | race  | care |acre|

####2. Create a list named anagramsList.
```java
LinkedList<LinkedList<Word>> anagramsList = new LinkedList<LinkedList<Word>>();
```
Initialization anagramsList
```java
for (int i = 0; i < wordsList.size(); i++) {
			LinkedList<Word> anagrams = new LinkedList<Word>();
			anagramsList.add(anagrams);
		}
```
Sort individual word and save each word in anagramsList
```java
for (int i = 0; i < wordsList.size(); i++) {
	for (int j = 0; j < wordsList.get(i).size(); j++) {
		String anagram = wordsList.get(i).get(j);
		char[] cArr = anagram.toCharArray();
		Arrays.sort(cArr);
		anagram = String.valueOf(cArr);
		Word w = new Word(i + 1, j, anagram);
		anagramsList.get(anagram.length() - 1).add(w);
	}
}
```
**anagramsList**

anagrams 0
words length is 1
Null

anagrams 1
words length is 2
Null

anagrams 2
words length is 3

| index |0|1| 2|
|:-----:|:-----:|:-----:|:-----:|
| position |0|1|2|
| length |3|3|3|
| word | act | act  | eeb |

anagrams 3
words length is 4

| index |0|1| 2|3|
|:-----:|:-----:|:-----:|:-----:|:-----:|
| position |0|1|2|3|
| length |4|4|4|4|
| word  |acer | acer | acer | eert |

####3. Sort each anagrams list.
```java
for (int i = 0; i < anagramsList.size(); i++) {
	Collections.sort(anagramsList.get(i));
}
```
**anagramsList**
 
anagrams 0
words length is 1
Null

anagrams 1
words length is 2
Null

anagrams 2
words length is 3

| index |0|1| 2|
|:-----:|:-----:|:-----:|:-----:|
| position |0|1|2|
| length |3|3|3|
| word | act | act  | eeb |

anagrams 3
words length is 4

| index |0|1| 2|3|
|:-----:|:-----:|:-----:|:-----:|:-----:|
| position |1|2|3|0|
| length |4|4|4|4|
| word  |acer | acer | acer | eert |

####4. Output result

It is similar to solutions_1

##Conclusion
As I know, the max size of List is `Integer.MAX_VALUE=2147483647`
There is no issue to deal with 10 Million Words. If it is over `Integer.MAX_VALUE=2147483647` which is 2 Billion Words, we may should use Hashmap and modularized program.




