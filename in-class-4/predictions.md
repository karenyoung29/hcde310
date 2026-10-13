# Class 4: Five broken snippets

Your name: Karen Young
Collaborator: Riley

# Part 1: Predict

**Don't run anything yet.** Read each snippet in `exercise.py` and write your guesses. A wrong guess is fine: the point is to compare.

## Snippet 1
- Which line breaks?
- What error will Python show? (the kind and the message)
- What's the fix?

Line 8.
Key error will be shown since "Room" is capitalized while the corresponding key is lowercase.
The fix is to make it "room" instead.

## Snippet 2
- Which line breaks?
- What error will Python show? (the kind and the message)
- What's the fix?

Line 12.
Type error will be shown since it is trying to add a string. 
The fix is to replace the + with a ,

## Snippet 3
- Which line breaks?
- What error will Python show? (the kind and the message)
- What's the fix?

Line 16.
Index error since the + 1 can make values be out of range.
The fix is to remove the + 1.

## Snippet 4
- Which line breaks?
- What error will Python show? (the kind and the message)
- What's the fix?

Line 29.
Name error since the parameter calls to visit, while the variable is visits.
Change either variable to match each other, whether it is visit or visits.


## Snippet 5
- Which line breaks?
- What error will Python show? (the kind and the message)
- What's the fix?

Line 40. 
Is there an initializing error? The method prints out data, but calling it while initializing a varaiable does not seem right.
The fix would be to initialize the variable first then call the method.

# Part 2: Run

Run `python3 exercise.py`. Python stops at the first error, so fix that snippet in `exercise.py`, run again, and see the next one. Fill in what actually happened.

## Snippet 1
- Which line broke?
- What error did Python show?
- What's the fix?

Line 8.
Key Error, Type Error (snippet 2 fix)
Make "Room" lowercase, then change the + to ,

## Snippet 2
- Which line broke?
- What error did Python show?
- What's the fix?

Line 12
Type Error
Change the + to ,

## Snippet 3
- Which line broke?
- What error did Python show?
- What's the fix?

Line 17.
Index Error
Remove all +1 of i


## Snippet 4
- Which line broke?
- What error did Python show?
- What's the fix?

Line 29.
Name Error
It says count_visits is not defined but it matches the method name and I don't know what else to change.

## Snippet 5
- Which line broke?
- What error did Python show?
- What's the fix?

Line 40 & Line 41.
Name Error
I tried fixing it by moving the method from initializing it to the print method but it still does not work. I also made it return instead of print and it still does not work and I'm stumped.


When all five are fixed, run `python3 check.py` until it says ✓.

Bonus: Snippet 5 prints something *before* it crashes. What, and why does it still crash?

# Part 3: Tutor practice (one snippet)

Pick one snippet. Write your guess first, then ask your tutor. Paste the chat (or a share link) below.

- Snippet #: 5
- Our guess before asking: It will say what the error is and how to fix it.
- Chat: Thanks for sharing your attempt. That’s the Try step done, and your code is well organized: a function with a docstring, a loop, and a comparison.

Now Predict. Before you run it, what exactly do you think this program will print? Please give me the exact output, including capitalization, and tell me which of the three titles you think it will be.
- Did it give you too much? What did you do?
It asked me to predict what the code will do and I responded.

Chat response: Thanks for committing to a prediction. That’s what the Predict step is for. Let’s test it, because a NameError is a specific claim.

A NameError usually means Python hit a name (a variable or function) that it doesn’t know about yet, often because of a typo or because it was never defined before being used.

So here’s my one question: which name in your code do you think Python wouldn’t recognize? Point to the exact line and the exact word, and tell me why you think it’s missing.

Once you’ve answered, run the code and tell me what actually prints.

My answer: Name error


