Reduction Function = int(H(password), 16) mod numOfPassword

Reduction Function will convert the hashed password into a long int and mod by the number of password.

Compile instructions:
1. Unzip the folder (if not program cannot compile properly)
2. Open Rainbow.py
3. Compile and run (u may either comment out generate_password_hash_reduction_function_table() in main() or not depending if you want to see the hash reduction function table)
4. Rainbow.txt will be created in the same folder after program finish running.

Program starts by printing the number of passwords and then generating and showing the hash reduction function table - def generate_password_hash_reduction_function_table():

Essentially this table will show the index, plaintext password, H(password) using MD5(https://www.geeksforgeeks.org/md5-hash-python/) and the reduction function index that points to the next plaintext password. 

Next, it will generate a hashChain by storing or removing the used and unused password into different lists. Thereafter, with the used and unused password it will generate a rainbow table and then write it into Rainbow.txt

Lastly, I have a function that prompts user to enter a 32 digit hexadecimal. if the user enter more than or less than 32 digits OR if the user enters anything that is not a hexadecimal(anything that is not 0,1,2,3 ... e,f) it will display an error message re-prompting for another 32 digit hashdigest.

On submit, the system will search if the hash digest is present in the rainbow table, if yes, it will get its corresponding password in the rainbow table and start to check if the hash of that is = to the hash digest entered by the user, if not it will hash and reduce till it finds a match.  system will also loop through the entire rainbow table plaintext, hash and reduce until it finds a match. If no match was found, it will send an show an appropriate message telling the user that it is unable to find a match.

Once found, it will display the pre-image of the hash digest to the user.