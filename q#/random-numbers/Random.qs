namespace Random{
    open Microsoft.Quantum.Intrinsic;
    open Microsoft.Quantum.Canon;
    open Microsoft.Quantum.Measurement;
    open Microsoft.Quantum.Math;

    operation randomize(totalBits:Int): Int
    {
        use q = Qubit[totalBits];
        mutable results = [];

        for bit in 0..(totalBits-1){
            H(q[bit]);
            set results += [M(q[bit])];
        }


        mutable result = 0;
        for bit in 0..(totalBits-1){
            mutable multiplier = 0;
            if(results[bit] == One) { set multiplier = 1; }

            set result += multiplier * PowI(2, bit);
        }
        
        return result;
        
    }
}