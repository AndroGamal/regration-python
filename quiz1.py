{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 56,
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 57,
   "metadata": {},
   "outputs": [],
   "source": [
    "def prepare_inputs(inputs):\n",
    "    # TODO: create a 2-dimensional ndarray from the given 1-dimensional list;\n",
    "    #       assign it to input_array\n",
    "    input_array = np.array(inputs)\n",
    "    \n",
    "    # TODO: find the minimum value in input_array and subtract that\n",
    "    #       value from all the elements of input_array. Store the\n",
    "    #       result in inputs_minus_min\n",
    "    inputs_minus_min = input_array-input_array.min()\n",
    "\n",
    "    # TODO: find the maximum value in inputs_minus_min and divide\n",
    "    #       all of the values in inputs_minus_min by the maximum value.\n",
    "    #       Store the results in inputs_div_max.\n",
    "    inputs_div_max = inputs_minus_min-input_array.max()\n",
    "\n",
    "    # return the three arrays we've created\n",
    "    return input_array, inputs_minus_min, inputs_div_max\n",
    "    \n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 58,
   "metadata": {},
   "outputs": [],
   "source": [
    "def multiply_inputs(m1, m2):\n",
    "    # TODO: Check the shapes of the matrices m1 and m2. \n",
    "    #       m1 and m2 will be ndarray objects.\n",
    "    #\n",
    "    #       Return False if the shapes cannot be used for matrix\n",
    "    #       multiplication. You may not use a transpose\n",
    "   \n",
    "    if m1.shape[0] != m2.shape[1] and m1.shape[1] != m2.shape[0]:\n",
    "        return False\n",
    "\n",
    "\n",
    "    # TODO: If you have not returned False, then calculate the matrix product\n",
    "    #       of m1 and m2 and return it. Do not use a transpose,\n",
    "    #       but you swap their order if necessary\n",
    "   \n",
    "    if m1.shape[1]== m2.shape[0]:\n",
    "        return np.matmul(m1, m2) \n",
    "    else:\n",
    "        return np.matmul(m2, m1) \n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 59,
   "metadata": {},
   "outputs": [],
   "source": [
    "def find_mean(values):\n",
    "    # TODO: Return the average of the values in the given Python list\n",
    "    return np.mean(values)\n",
    "        \n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 60,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Input as Array: [-1  2  7]\n",
      "Input minus min: [0 3 8]\n",
      "Input  Array: [-7 -4  1]\n",
      "Multiply 1:\n",
      "False\n",
      "Multiply 2:\n",
      "[[14]\n",
      " [32]]\n",
      "Multiply 3:\n",
      "[[ 9 12 15]]\n",
      "Mean == 2.6666666666666665\n"
     ]
    }
   ],
   "source": [
    "\n",
    "input_array, inputs_minus_min, inputs_div_max = prepare_inputs([-1,2,7])\n",
    "print(\"Input as Array: {}\".format(input_array))\n",
    "print(\"Input minus min: {}\".format(inputs_minus_min))\n",
    "print(\"Input  Array: {}\".format(inputs_div_max))\n",
    "\n",
    "print(\"Multiply 1:\\n{}\".format(multiply_inputs(np.array([[1,2,3],[4,5,6]]), np.array([[1],[2],[3],[4]]))))\n",
    "print(\"Multiply 2:\\n{}\".format(multiply_inputs(np.array([[1,2,3],[4,5,6]]), np.array([[1],[2],[3]]))))\n",
    "print(\"Multiply 3:\\n{}\".format(multiply_inputs(np.array([[1,2,3],[4,5,6]]), np.array([[1,2]]))))\n",
    "\n",
    "print(\"Mean == {}\".format(find_mean([1,3,4])))"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
