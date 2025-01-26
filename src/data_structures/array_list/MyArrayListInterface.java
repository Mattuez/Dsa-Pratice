package data_structures.array_list;

public interface MyArrayListInterface<T> {
    T add(T element);

    // Insere um elemento em uma posição específica
    T add(int index, T element);

    // Retorna o elemento na posição especificada
    T get(int index);

    // Remove o elemento na posição especificada
    void remove(int index);

    // Substitui o elemento na posição especificada por um novo valor
    T set(int index, T element);

    // Retorna o tamanho atual da lista
    int length();

    // Verifica se a lista está vazia
    boolean isEmpty();

    // Verifica se a lista está cheia
    boolean isFull();

    // Aumenta o tamanho do array de items
    void grow();

    // Verifica se a lista contém um elemento específico
    boolean contains(T element);


    // Limpa todos os elementos da lista
    void clear();
}
