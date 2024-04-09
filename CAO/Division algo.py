from tabulate import tabulate

def decimal_to_twos_complement_binary(num, n):
    bin_equivalent = bin(abs(num))[2:].zfill(n)
    if num < 0:
        inverted_str = ''.join(['0' if bit == '1' else '1' for bit in bin_equivalent])
    # Add 1 to the inverted binary to get two's complement
        inverted_binary = bin(int(inverted_str, 2) + 1)[2:].zfill(n)
        bin_equivalent = inverted_binary
    return bin_equivalent

def restoring_algorithm(A, Q,M_dash,negative_M,n,data):
    no_of_bits=n
    while n>0:
        n-=1
        A,Q=left_shift(A,Q)
        A= bin(int(A, 2) + int(negative_M,2))[2:].zfill(no_of_bits)
        if len(A)>no_of_bits:
            setter=len(A)-no_of_bits
            A= A[setter:].zfill(no_of_bits)

        #checking if we need to restore and deciding the value of Q_0 accordingly
        bit = A[0]
        if bit == '0':
           Q=Q+'1'
           step=f'No neded to restore. Count: {n}'

        elif bit == "1":
            #Restore as A is negative
            Q=Q+'0'
            step=f'Value of A restored. Count: {n}'
            A= bin(int(A, 2) + int(M_dash,2))[2:].zfill(no_of_bits)
            if len(A)>no_of_bits:
                setter=len(A)-no_of_bits
                A= A[setter:].zfill(no_of_bits)
        data.append([A, Q,step])
    return data

def left_shift(A,Q):
     A,Q=str(A),str(Q)
     A = A[1:] + Q[0]
     Q = Q[1:]
     return A,Q 

def Non_restoring_algorithm(A, Q,M_dash,negative_M,n,data):
  no_of_bits=n
  while n>0:
    n-=1
    bit=A[0]
    A,Q=left_shift(A,Q)
    #check if A<0
    if bit=='0':
       A= bin(int(A, 2) + int(negative_M,2))[2:]
       if len(A)>no_of_bits:
            setter=len(A)-no_of_bits
            A= A[setter:].zfill(no_of_bits)
       step=f'A <-- A-M. Count:{n}'
    else:
        A= bin(int(A, 2) + int(M_dash,2))[2:]
        if len(A)>no_of_bits:
            setter=len(A)-no_of_bits
            A= A[setter:]
        step=f'A <-- A+M. Count:{n}'

    #check if A<0 again
    bit=A[0]
    if bit=='0':
       Q=Q+'1'
    else:
       Q=Q+'0'
    data.append([A, Q,step])
  #after n iterations check if remainder is negative, if yes restore
  if A[0]=='1':
    A= bin(int(A, 2) + int(M_dash,2))[2:].zfill(no_of_bits)
    if len(A)>no_of_bits:
        setter=len(A)-no_of_bits
        A= A[setter:]
        step=f'Special restore.A <-- A-M. Count:{n}'
        data[-1]=[A,Q,step]
  return data
    
def main():
    #exceptional cases handled
    try:
     choice=int(input('Enter 0 for Restoring algorithm and 1 & for Non Restoring algorith: '))
     Q = int(input('Enter the Dividend: '))
     M = int(input('Enter the Divisor: '))

     if M < 0 or Q < 0:
        raise ValueError("Both divisor and dividend must be positive")
     elif Q==0:
        raise ValueError("Divisor can not be 0")
     elif choice!=1 and choice!=0:
        raise ValueError('Select the Algorithm properly')
     
    except ValueError as errormsg:
     print("\nError:", errormsg)
    
    else:
    #logic to decide no of steps
     if Q>M:
        n=len(bin(Q)[2:])
     else:
        n=len(bin(M)[2:])+1
     A="0".zfill(n)

    #covert to binary
     M_dash= bin(M)[2:].zfill(n)
     Q_dash= bin(Q)[2:].zfill(n)
     negative_M=decimal_to_twos_complement_binary(int(-M),n)
     print(f'{Q} in binary: {Q_dash} ')
     print(f'{M} in binary: {M_dash}')
     print(f'{-M} in binary: {negative_M} ')

     data=[["A", "Q","Step"],[A,Q_dash,f'Values initialised. Count:{n}']]
     if choice==0:
      name='Restoring'
      table_data=restoring_algorithm(A, Q_dash, M_dash,negative_M,n,data)
     else:
      name='Non Restoring'
      table_data=Non_restoring_algorithm(A, Q_dash, M_dash,negative_M,n,data)
     #to print the algorithm steps in tabular format
     table = tabulate(table_data, tablefmt='grid')
     print(table)
     Quotient=str(data[-1][1])
     Remainder=str(data[-1][0])
     print(f'By {name} algorithm:\nThe Quotient is: {Quotient} in decimal {int(Quotient,2)}')
     print(f'The Remainder is: {Remainder} in decimal {int(Remainder,2)}')

if __name__ == "__main__":
    main()



