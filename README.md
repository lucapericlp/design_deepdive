# Design Patterns

In a want for improving software engineering ability to write more optimized code, I've begun reading [Design Patterns: Elements of Reusable Object-Oriented Software](https://www.amazon.com/dp/0201633612/?tag=stackoverfl08-20) and will be implementing different design patterns in Python3.


Current Patterns
----------------

__Creational Patterns__:

<!-- 
| Pattern | Description |
|:-------:| ----------- |
| [abstract_factory](patterns/creational/abstract_factory.py) | use a generic function with specific factories |
| [borg](patterns/creational/borg.py) | a singleton with shared-state among instances |
| [builder](patterns/creational/builder.py) | instead of using multiple constructors, builder object receives parameters and returns constructed objects |
| [factory_method](patterns/creational/factory_method.py) | delegate a specialized function/method to create instances |
| [lazy_evaluation](patterns/creational/lazy_evaluation.py) | lazily-evaluated property pattern in Python |
| [pool](patterns/creational/pool.py) | preinstantiate and maintain a group of instances of the same type |
| [prototype](patterns/creational/prototype.py) | use a factory and clones of a prototype for new instances (if instantiation is expensive) | -->

__Structural Patterns__:
<!-- 
| Pattern | Description |
|:-------:| ----------- |
| [3-tier](patterns/structural/3-tier.py) | data<->business logic<->presentation separation (strict relationships) |
| [adapter](patterns/structural/adapter.py) | adapt one interface to another using a white-list |
| [bridge](patterns/structural/bridge.py) | a client-provider middleman to soften interface changes |
| [composite](patterns/structural/composite.py) | lets clients treat individual objects and compositions uniformly |
| [decorator](patterns/structural/decorator.py) | wrap functionality with other functionality in order to affect outputs |
| [facade](patterns/structural/facade.py) | use one class as an API to a number of others |
| [flyweight](patterns/structural/flyweight__py3.py) | transparently reuse existing instances of objects with similar/identical state |
| [front_controller](patterns/structural/front_controller.py) | single handler requests coming to the application |
| [mvc](patterns/structural/mvc.py) | model<->view<->controller (non-strict relationships) |
| [proxy](patterns/structural/proxy.py) | an object funnels operations to something else | -->

__Behavioral Patterns__:
<!-- 
| Pattern | Description |
|:-------:| ----------- |
| [chain_of_responsibility](patterns/behavioral/chain_of_responsibility__py3.py) | apply a chain of successive handlers to try and process the data |
| [catalog](patterns/behavioral/catalog.py) | general methods will call different specialized methods based on construction parameter |
| [chaining_method](patterns/behavioral/chaining_method.py) | continue callback next object method |
| [command](patterns/behavioral/command.py) | bundle a command and arguments to call later |
| [iterator](patterns/behavioral/iterator.py) | traverse a container and access the container's elements |
| [mediator](patterns/behavioral/mediator.py) | an object that knows how to connect other objects and act as a proxy |
| [memento](patterns/behavioral/memento.py) | generate an opaque token that can be used to go back to a previous state |
| [observer](patterns/behavioral/observer.py) | provide a callback for notification of events/changes to data |
| [publish_subscribe](patterns/behavioral/publish_subscribe.py) | a source syndicates events/data to 0+ registered listeners |
| [registry](patterns/behavioral/registry__py3.py) | keep track of all subclasses of a given class |
| [specification](patterns/behavioral/specification.py) |  business rules can be recombined by chaining the business rules together using boolean logic |
| [state](patterns/behavioral/state.py) | logic is organized into a discrete number of potential states and the next state that can be transitioned to |
| [strategy](patterns/behavioral/strategy.py) | selectable operations over the same data |
| [template](patterns/behavioral/template.py) | an object imposes a structure but takes pluggable components |
| [visitor](patterns/behavioral/visitor.py) | invoke a callback for all items of a collection | -->
