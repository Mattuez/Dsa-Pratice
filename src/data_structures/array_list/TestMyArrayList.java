package data_structures.array_list;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

public class TestMyArrayList {

    @Test
    void testAddMethod() {
        MyArrayListInterface<Integer> myArrayList = new MyArrayList<>(2);

        myArrayList.add(10);
        myArrayList.add(20);
        myArrayList.add(30);

        System.out.println("Hello world");
    }

    @Test
    void testAddMethodWithIndex() {
        MyArrayListInterface<Integer> myArrayList = new MyArrayList<>(5);

        myArrayList.add(5);
        myArrayList.add(10);
        myArrayList.add(20);
        myArrayList.add(25);
        myArrayList.add(30);

        myArrayList.add(2, 15);

        System.out.println("Hello world");
    }

    @Test
    void testRemoveMethod() {
        MyArrayListInterface<Integer> myArrayList = new MyArrayList<>(5);

        myArrayList.add(5);
        myArrayList.add(10);
        myArrayList.add(20);
        myArrayList.add(25);
        myArrayList.add(30);

        myArrayList.remove(1);

        System.out.println("Hello world");
    }

    @Test
    void testGetMethod() {
        MyArrayListInterface<Integer> myArrayList = new MyArrayList<>(2);

        myArrayList.add(10);
        assert myArrayList.get(0) == 10;

        assertThrows(IndexOutOfBoundsException.class, () -> myArrayList.get(1));
        assertThrows(IndexOutOfBoundsException.class, () -> myArrayList.get(-1));
    }
}
