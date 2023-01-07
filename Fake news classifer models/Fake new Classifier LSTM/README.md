
Long Short Term Memory networks – usually just called “LSTMs” – are a special kind of recurrent neural networks, capable of learning long-term dependencies. LSTMs are explicitly designed to

capture long-term connections

help avoid the vanishing gradient problems

Rather than dealing the gradient issues directly, the architectures of recurrent neural networks are modified to have a better gradient flow properties.

All recurrent neural networks have the form of a chain of repeating modules of neural network. In standard recurrent neural networks, this repeating module will have a very simple structure, such as a single tanh layer.


LSTMs have similar chain like structure. However, instead of having a single tanh layer, there are four interacting layers.

![image](https://user-images.githubusercontent.com/121180975/209126657-2089f20d-1b30-45c8-8879-e03fe08c5e0e.png)
