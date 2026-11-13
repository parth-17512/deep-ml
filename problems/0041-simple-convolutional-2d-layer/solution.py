import numpy as np
def simple_conv2d(input_matrix: np.ndarray, kernel: np.ndarray, padding: int, stride: int):

    input_height, input_width = input_matrix.shape
    kernel_height, kernel_width = kernel.shape

    # Step 1: Add zero padding
    padded_matrix = np.pad(
        input_matrix,
        pad_width=padding,
        mode="constant",
        constant_values=0
    )

    # Step 2: Calculate output dimensions
    padded_height, padded_width = padded_matrix.shape

    output_height = (padded_height - kernel_height) // stride + 1
    output_width = (padded_width - kernel_width) // stride + 1

    # Step 3: Initialize output matrix
    output_matrix = np.zeros((output_height, output_width))

    # Step 4: Perform convolution
    for i in range(output_height):
        for j in range(output_width):

            # Find the current region
            row_start = i * stride
            col_start = j * stride

            region = padded_matrix[
                row_start:row_start + kernel_height,
                col_start:col_start + kernel_width
            ]

            # Element-wise multiplication and sum
            output_matrix[i, j] = np.sum(region * kernel)

    return output_matrix