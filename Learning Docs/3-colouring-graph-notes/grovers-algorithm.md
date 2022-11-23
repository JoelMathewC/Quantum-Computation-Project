# Grover's Algorithm

Improves unstructured database search from O(N) to O(root(N)). A quadratic speedup. A nice article can be found [here](https://qiskit.org/textbook/ch-algorithms/grover.html)

## Prerequisites
### Oracle Function
An oracle is a black box that takes an input and produces an output.

Let x represent all the values we are not looking for and w the value that we are looking for. Then the oracle function is given by f which
```
f(x) = 0
f(w) = 1
```

### Amplitude Amplification
This is a way to increase the probability of observing the correct answer and decrease other probabilities.

![image](assets/amplitude-amplification.png)

**Step 1:** Assign a phase of -1 to the chosen ket. (Ket as in |00> or |01> or any of those). Lets call matrix that does phase flip as Uf.

**Step 2:** Find mean of all probability amplitudes

**Step 3:** Invert all probability amplitudes about the mean. The matrix here is called U(phi) \[Also called diffusion operator\]

## Performing the search
There are two steps to Grover's Algorithm/Grover's Search

1. Pass the qubits (all |0>) through a Hardamard gate to put them in superposition (|s>) (image1). This essentially puts the amplitude of all the states at 25% (image2)

![image](assets/grover-step1.png)

![image](assets/grover-step1-result.png)

2. We use a phase flip oracle as defined below (image3). This oracle flips the phase of all the value that we are searching for and keeps the phases of the other values the same(image4).

![image](assets/Grover-step2.png)

![image](assets/grover-step2-result.png)

3. He apply the Hardamard gates again on the qubits and this flips back the input we are looking for with an amplified amplitude. This essentially is just reflecting the about the original |s> vector.

![image](assets/grover-step3.png)
![image](assets/grover-step3-result.png)

4. Repeat step 2 and 3 till the probability comes very close to 1 and then measuring should give us the output that we are looking for. It can now be ascertained that when doing a search in a list running this function root(N) times is sufficient to get the corresponding output.

![image](assets/grover-step4.png)