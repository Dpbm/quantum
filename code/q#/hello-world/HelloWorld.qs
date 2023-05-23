namespace HelloWorld {
    open Microsoft.Quantum.Intrinsic;
    open Microsoft.Quantum.Canon;

    operation SayHello(name: String): Unit{
        Message($"Hello, {name}!!!!");
    }

}
