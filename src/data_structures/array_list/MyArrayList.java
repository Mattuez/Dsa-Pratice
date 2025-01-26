package data_structures.array_list;

import java.util.Objects;

public class MyArrayList<T> implements MyArrayListInterface<T> {

    private T[] items;
    private Integer length;
    private Integer capacity;

    @SuppressWarnings("unchecked")
    public MyArrayList() {
        this.capacity = 10;
        this.length = 0;

        this.items = (T[]) new Object[this.capacity];
    }

    @SuppressWarnings("unchecked")
    public MyArrayList(Integer capacity) {
        this.capacity = capacity;
        this.length = 0;

        this.items = (T[]) new Object[this.capacity];
    }

    @Override
    public T add(T element) {
        if (this.isFull()) {
            this.grow();
        }

        items[this.length] = element;
        length++;

        return items[this.length - 1];
    }

    @Override
    public T add(int index, T element) {
        if (this.isFull()) {
            this.grow();
        }

        if (index > this.length || index < 0) {
            throw new IndexOutOfBoundsException("Index out of bounds");
        }

        for (int i = this.length; i > index; i--) {
            items[i] = items[i - 1];
        }

        items[index] = element;
        length++;

        return items[index];
    }

    @Override
    public T get(int index) {
        if (index >= this.length || index < 0) {
            throw new IndexOutOfBoundsException("Index out of bounds");
        }

        return this.items[index];
    }

    @Override
    public void remove(int index) {
        if (index >= this.length || index < 0) {
            throw new IndexOutOfBoundsException("Index out of bounds");
        }

        for (int i = index; i < this.length - 1; i++) {
            this.items[i] = this.items[i + 1];
        }

        this.items[length - 1] = null;

        length--;
    }

    @Override
    public T set(int index, T element) {
        if (index >= this.length || index < 0) {
            throw new IndexOutOfBoundsException("Index out of bounds");
        }

        this.items[index] = element;

        return this.items[index];
    }

    @Override
    public int length() {
        return this.length;
    }

    @Override
    public boolean isEmpty() {
        return this.length == 0;
    }

    @Override
    public boolean isFull() {
        return Objects.equals(this.length, this.capacity);
    }

    @SuppressWarnings("unchecked")
    @Override
    public void grow() {
        T[] new_items = (T[]) new Object[this.capacity * 2];

        for (int i = 0; i < this.capacity; i++) {
            new_items[i] = this.items[i];
        }

        this.items = new_items;
        this.capacity = this.capacity * 2;
    }

    @Override
    public boolean contains(T element) {
        for (int i = 0; i < length; i++) {
            if (element.equals(items[i])) {
                return true;
            }
        }

        return false;
    }

    @SuppressWarnings("unchecked")
    @Override
    public void clear() {
        this.items = (T[]) new Object[this.capacity];
        this.length = 0;
    }
}
