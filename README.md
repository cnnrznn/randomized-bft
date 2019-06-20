# randomized-bft
A Python implementation of one of Bracha's randomized consensus protocols

Consensus protocols are important for protecting otherwise good code from the
perils of the real world. Power, disk, human, and other failures inevitably
cause programs to go screwy, so it is necessary that those programs be resilient
to such benign (and sometimes malicious) faults. In order to achieve such
resilience we must replicate our program and its data. This project is an
implementation of the protocol found in this paper by Bracha [1] that describes
two randomized protocols for the crash and byzantine fault models. This project
is an implementation for the latter.

[1] _Asynchronous consensus and broadcast protocols_, 1985.
