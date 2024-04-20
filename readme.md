Turns out producing a decent (even if not professionally) looking multi-level pie chart isn't as trivial as one might
think.

This repo presents a quite minimal example for producing a 2 level pie-chart for one's professional experience,
where the inner ring represents the category of the workplace (e.g., startup, enterprise, etc.), and the outer ring
represents the different workplaces/companies (e.g., Coca-Cola, PayPal, etc.)

The following code:

```python
from expierience import Position, PieChart

positions = [
    Position(company="Enterprise1", tenure=2, type="Enterprise"),
    Position(company="Enterprise2", tenure=2, type="Enterprise"),
    Position(company="Startup1", tenure=3, type="Startup"),
    Position(company="Startup2", tenure=1, type="Startup"),
    Position(company="Startup2", tenure=1.5, type="Startup"),
]

PieChart(positions).make()
```

produces the following image:

![Two level pie chart](example.png.)