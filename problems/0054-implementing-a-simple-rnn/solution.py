
import numpy as np

def rnn_forward(
    input_sequence: list[list[float]],
    initial_hidden_state: list[float],
    Wx: list[list[float]],
    Wh: list[list[float]],
    b: list[float]
) -> list[float]:

    # Step 1: Convert inputs into NumPy arrays
    input_sequence = np.array(input_sequence, dtype=float)
    hidden_state = np.array(initial_hidden_state, dtype=float)
    Wx = np.array(Wx, dtype=float)
    Wh = np.array(Wh, dtype=float)
    b = np.array(b, dtype=float)

    # Step 2: Process each input in the sequence
    for x_t in input_sequence:

        # Step 3: Calculate new hidden state
        hidden_state = np.tanh(
            np.dot(Wx, x_t) +
            np.dot(Wh, hidden_state) +
            b
        )

    # Step 4: Return final hidden state
    return hidden_state.tolist()
