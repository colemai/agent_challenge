<h1> Agent based coding exercise </h1>



<strong>To install the requirements:</strong>

```python -m pip install -r requirements.txt```

<strong>To run:</strong> 

```python src/main.py path_to_json```

e.g

```python src/main.py data/tiny-tines-sunset.json```

<strong>To test:</strong>

```pytest```




Hypothetical next steps:
1. Account for further edge cases and errors, CI pipeline
2. Create a log to help with debugging
3. Optimise and adapt for scale 
 

To scale this on a single machine I'd make it more modular - one agent per proc. I was toying with the idea of turning the 'agents' into true, persistent programmes listening on a port each. Manually scale each agent type according to expected usage, use a hash table to distribute the load among the ports of agents of the same time.

Though in a real life situation I'd stick to Kubernetes

Depending on the usecase and the relative demands on I/O, CPU, Mem, Network, it might be worth re-writing some aspects in Go or C


