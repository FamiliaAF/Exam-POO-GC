## Sección 1: Preguntas Teóricas (10 puntos)

### ¿Qué es una clase en POO y cuál es su propósito?
Una clase en programación orientada a objetos (POO) es como un plano o plantilla que define las características y comportamientos de un conjunto de objetos. Es decir, es una descripción abstracta de un tipo de entidad. Su propósito principal es encapsular los datos (atributos) y las operaciones (métodos) que definen a un objeto.

### 2.Define qué es un objeto y cómo se relaciona con una clase.
Un objeto es una representación de algo real o ficticio. Es como crear una copia de ese plano o plantilla, pero con valores específicos para sus atributos. Por ejemplo, si la clase es "Perro", un objeto sería un perro en particular con un nombre, raza, color, etc. La relación es que un objeto "pertenece a" una clase.

### 3.¿Qué son los atributos de una clase? Proporciona un ejemplo.
Los atributos de una clase son las características o propiedades que definen a los objetos de esa clase. Son como las variables de una clase y almacenan datos. Por ejemplo, en la clase "Coche", los atributos podrían ser: marca, modelo, color, año. Nos dicen cómo es el objeto.

### 4.Explica qué es un método en POO y para qué se utiliza.
Un método en POO es una función asociada a una clase. Define las acciones o comportamientos que pueden realizar los objetos de esa clase. Por ejemplo, en la clase "Coche", los métodos podrían ser: arrancar(), acelerar(), frenar().

### 5.¿Qué significa el término encapsulamiento? ¿Por qué es importante?
El encapsulamiento es el principio de ocultar los detalles internos de una clase y exponer solo una interfaz para interactuar con ella. Es decir, los atributos y métodos se pueden marcar como privados o públicos para controlar el acceso. Es importante porque:
* **Protege los datos:** Evita modificaciones accidentales de los atributos.
* **Aumenta la reutilización:** Permite cambiar la implementación interna sin afectar el código que lo utiliza.
* **Facilita el mantenimiento:** Hace el código más legible y fácil de entender.

### 6.Describe el concepto de herencia y da un ejemplo de su uso.
La herencia es un mecanismo que permite crear nuevas clases (clases derivadas o hijas) a partir de clases existentes (clases base o padres). La clase hija hereda todos los atributos y métodos de la clase padre y puede agregar nuevos o modificar los existentes. Por ejemplo, si tenemos una clase "Animal" y una clase "Perro", "Perro" puede heredar de "Animal" y agregar atributos específicos como "raza".

### 7.¿Cuál es la diferencia entre una clase base (padre) y una clase derivada (hija)?
La clase base es la clase de la cual se hereda. Define las características y comportamientos comunes a un grupo de clases. La clase derivada es la clase que hereda de la clase base. Puede especializar o ampliar las características y comportamientos de la clase base.

### 8.¿Qué son los métodos __init__ y __str__ en Python y cuál es su función en una clase?
* **__init__**: Es el constructor de una clase. Se ejecuta automáticamente cuando se crea un objeto de esa clase. Se utiliza para inicializar los atributos del objeto.
* **__str__**: Define la representación en cadena de un objeto. Es decir, cómo se muestra el objeto cuando se imprime.

### 9.Explica qué es la sobrecarga de métodos y cómo se logra en Python.
La sobrecarga de métodos permite definir múltiples métodos con el mismo nombre pero con diferentes parámetros. Python determina qué método ejecutar en función de los argumentos proporcionados. Se logra simplemente definiendo múltiples métodos con el mismo nombre pero con diferentes listas de parámetros.

### 10.¿Qué es un constructor y cómo se puede implementar en POO?
Un constructor es un método especial que se utiliza para inicializar los objetos de una clase. Se llama automáticamente cuando se crea un nuevo objeto. En Python, el constructor se define con el nombre `__init__`.