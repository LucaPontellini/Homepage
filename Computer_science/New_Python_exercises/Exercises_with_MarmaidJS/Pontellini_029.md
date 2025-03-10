Creare un programma di trading automatizzato che utilizza flussi economici per prendere decisioni d'acquisto e vendita.
Il programma deve implementare strategie di trading semplici e includere funzioni di gestione del rischio.
Crea relativo diagramma UML.

```mermaid
classDiagram

    class TradingPlatform {
            +users: list[User]
            +coins: list[Coin]
            +trading_strategies: list[TradingStrategy]
            +execute_trades()
            +manage_risk(user: User, coin: Coin)
            +print_all_the_coins_history()
        }

    class User {
        +username: str
        +email: str
        +password: str
        +profile: str
        +transaction_history: list
        +wallet: Wallet
        +register()
        +create_profile()
        +add_budget()
        +purchase(coin: Coin): Coin
        +sale(coin: Coin)
    }

    class Wallet {
        +balance: float
        +transactions: list
        +deposit(amount: float)
        +withdraw(amount: float)
        +get_balance(): float
    }

    class Coin {
        +typology: list[str]
        +value: float
        +coin_history: list[float]
        +change_value(coin_history: list[float])
    }

    class TradingStrategy {
        +strategy_name: str
        +parameters: dict
        +apply_strategy(user: User, coin: Coin): bool
    }

    class Risk {
        +stop_loss: float
        +take_profit: float
        +capital_allocation: float
        +apply_risk(user: User, coin: Coin)
    }

TradingPlatform "1..*" --> "1..*" TradingStrategy: implements
TradingPlatform "1..*" --> "1..*" Risk: incorporates
TradingPlatform "1..*" --> "1..*" User: provides access
TradingPlatform "1..*" --> "1..*" Coin: manages
User "1..*" --> "1..*" Wallet: possesses
User "1..*" --> "0..*" TradingStrategy: can apply
User "1..*" --> "0..*" Risk: can have
Wallet "0..*" --> "1..*" TradingPlatform: integrates with
Coin "0..*" --> "0..*" Wallet: are contained in
```