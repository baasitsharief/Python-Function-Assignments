# Python Function Assignments

Assignment questions and their solutions based on CRUX's python course taught during summer of 2017

## Questions

1. Write a method “is_divisible” that takes two integers, m and n. The method returns True if m is divisible by n, and returns False otherwise.

2. Write a function called “yikes” that has one argument ‘x’ to calculate the following:
	xe−x + sqrt(1 − e−x)
Return the result obtained. 
Example : yikes(5) should return 1.0303150673.
Use ‘math’ module.

3. Write a function “roots” that computes the roots of a quadratic equation and prints them. In case of non-real roots print an error message instead, saying that the roots are non-real. Take three arguments {a,b,c} such that
ax2 + bx + c = 0
Bonus – Compute and print non-real roots. Python can handle complex number. Google away!

4. Write a function to calculate and print GPA for a semester. Take three arguments : number of courses(n), a list of credits for n courses, another list for grade point obtained(out of 10) of n courses.
Print “sed_lyf” if GPA is lesser than 5. Print “GGWP” if GPA is greater than 9.

5. Write a method “roll_dice” that takes in 2 parameters - the number of sides of the die(n), and the number of dice to roll(m) - and generates ‘m’ random roll values for each die rolled. Print out each roll and then return the string “That’s all!”. If the number of sides is less than 4, print an error message and terminate the program. 
 Example :

>>> roll_dice(5,3)
2
4
1
“That’s all”

6. Write a function “pygLatin” that takes in a single word, then converts the word to PygLatin.
PygLatin is a secret language in which we take the first letter of a word, put it at the end, and append “ay”. The only exception is if the first letter is a vowel, in which case we keep it as it is and append “hay” to the end. Additionally, all upper case characters are converted to lower case in PygLatin. Any characters other than alphabets remain unchanged.
E.g. “boot” → “ootbay”,  “image” → “imagehay”, “GgWp”→ “gwpgay”
Bonus – Make a PygLatin translator function “pygLatin_sentence” for a sentence, using the “pygLatin” function. 
E.g. “I am a 9 pointer.” → “ihay amhay ahay 9 ointerpay.”
Double Bonus – Extend this functionality to translate paragraphs containing multiple sentences to PygLatin.  

