from expierience import Position, PieChart

positions = [
    Position(company="Enterprise1", tenure=2, type="Enterprise"),
    Position(company="Enterprise2", tenure=2, type="Enterprise"),
    Position(company="Startup1", tenure=3, type="Startup"),
    Position(company="Startup2", tenure=1, type="Startup"),
    Position(company="Startup2", tenure=1.5, type="Startup"),
]

PieChart(positions).make()
