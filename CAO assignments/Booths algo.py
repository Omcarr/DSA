from tabulate import tabulate

def decimal_to_twos_complement_binary(num, n):
    bin_equivalent = bin(abs(num))[2:].zfill(n)
    if num < 0:
        inverted_str = ''.join(['0' if bit == '1' else '1' for bit in bin_equivalent])
    # Add 1 to the inverted binary to get two's complement
        inverted_binary = bin(int(inverted_str, 2) + 1)[2:].zfill(n)
        bin_equivalent = inverted_binary
    return bin_equivalent

def twos_complement_binary_to_decimal(num, n):
    decimal_equivalent = int(num, 2)
    if num[0] =='1':
        # remove 1 to get the 1's complement
        num=bin(int(num, 2) - 1)[2:].zfill(n)
        num = ''.join(['0' if bit == '1' else '1' for bit in num])
        decimal_equivalent =f'-{int(num, 2)}'
    return decimal_equivalent

def booths_algorithm(A, Q, B, Q_1,negative_B,n,data):
    count=n
    while count>0:
        count-=1
    # Check the last two bit of Q and Q_1
        bits = Q[-1] + Q_1
        if bits == "00" or bits == "11":
           Q_1,Q,A=right_shift(Q_1,Q,A)
           step=f'Arithmetic Right shift. Count: {count}'

        elif bits == "01":
            A = bin(int(A, 2) + int(B,2))[2:].zfill(n)
            if len(A)>n:
             setter=len(A)-n
             A= A[setter:]
            Q_1,Q,A=right_shift(Q_1,Q,A)
            step=f'Arithmetic Right shift & A<--A+B. Count: {count}'
            
        elif bits == "10":
            A= bin(int(A, 2) + int(negative_B,2))[2:].zfill(n)
            if len(A)>n:
             setter=len(A)-n
             A= A[setter:]
            Q_1,Q,A=right_shift(Q_1,Q,A)
            step=f'Arithmetic Right shift & A<--A-B. Count: {count}'
        data.append([A, Q, Q_1,step])
    return data

def right_shift(Q_1,Q,A):
     Q_1,Q,A=str(Q_1),str(Q),str(A)
     Q_1=Q[-1]
     Q = A[-1]+ Q[:-1]
     A = A[0] + A[:-1]
     return Q_1,Q,A  

def main():
    B = int(input('Enter the Multiplicand: '))
    Q = int(input('Enter the Multiplier: '))
    #logic to decide no of steps
    if abs(B)>abs(Q):
        temp=B
    else:
        temp=abs(Q)
    n=len(bin(temp)[2:])+1
    A="0".zfill(n)
    Q_1="0"

    #Convert B, -B, and Q to two's complement binary
    B_dash = decimal_to_twos_complement_binary(int(B), n)
    negative_B = decimal_to_twos_complement_binary(-int(B), n)
    Q_dash = decimal_to_twos_complement_binary(int(Q), n)

    print(f'{B} in binary: {B_dash} ')
    print(f'{Q} in binary: {Q_dash}')
    print(f'{-B} in binary: {negative_B} ')
    data=[["A", "Q", "Q_1","Step number"],[A, Q_dash, Q_1,f'Values initialised. Count:{n}']]
    table_data=booths_algorithm(A, Q_dash, B_dash, Q_1, negative_B, n,data)
    table = tabulate(table_data, tablefmt='grid')
    print(table)
    Answer=f'{data[-1][0]}{data[-1][1]}'
    answer_decimal=twos_complement_binary_to_decimal(Answer,n)
    print(f'The answer is: {Answer}')
    print(f'By Booths algotrirthm the answer is: {answer_decimal}')

if __name__ == "__main__":
    main()



