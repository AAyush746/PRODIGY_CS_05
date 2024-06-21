def alphabet_number(text):
    if text.isalpha() and len(text)==1:
            
        return ord(text.upper())-ord("A")+1
    else:
        raise ValueError("input must be single alphabet character")


def number_alphabet(num):
    if 1<=num<=26:
        return chr(num+ord('A')-1)
    else :
        raise ValueError("input number must be number between 1 and 26")
    
def decrypted(Plain_text,K):
    total=[]
    if (Plain_text is None):
            return -1
    # input(print("enter the plain text"))
    for char in Plain_text:
        if char.isalpha():
        # plain_text=plain_text+K
            # input1=Plain_text.split()
            number_format=alphabet_number(char)
            number_format=(number_format-K)%26
            output=number_alphabet(number_format)
            
            
        if char.islower():
            output=output.lower()
            total.append(output)
        elif char.isupper():
            output=output.upper()
            total.append(output)
            
        else:
            total.append(char) 
   
    return ''.join(total)


def main():
    user_input=input("enter the text ")
    n=int(input("enter the desirable ceaser cypher"))
    
    print("your input in decrypted form is :")
    print(decrypted(user_input,n))

if __name__=="__main__":
    main()
            
          