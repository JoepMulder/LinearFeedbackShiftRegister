
class Crypto:
    def lfsr(self, c, s, l=20):
        
        output = []
        for i in range(l):
            
            # Add s[0] to output
            output.append(s[0]) 

            # Calculate new bit to put at the end of the register
            new_bit = s[0] * c[len(c)-1]
            for i in range(1, len(c)):
                new_bit = 1 if new_bit != s[i] * c[len(c)-i-1] else 0

            # Shift register and append the new bit 
            s = s[1:len(s)] + [new_bit]

        return output
    
if __name__ == '__main__':
    crypto = Crypto()

    # NOTE: c array input should be like [c1, c2, ...., cL]
    c = [0,1,0,0,1,1,0,1,1,0]

    # NOTE: s array input should be like [s0, s1, ...., sL-1]
    s = [0,1,1,0,0,1,0,1,0,1]

    
    output = crypto.lfsr(c, s, 40)
    print("Final output:")
    print(output)
    
    
    
    

