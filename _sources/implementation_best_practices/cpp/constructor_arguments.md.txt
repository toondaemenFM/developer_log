# Passing constructor arguments

## Example 1
```
A::A() {}
B::B(std::shared_ptr<A> a) : a_(a) {}

C::C()
{
  a_ = std::make_shared<A>();
  b_ = std::make_unique<B>(a_);
}
```

- C passes a copy of a_ to B. The reference count of the pointer is incremented (1 -> 2).
- The constructor of B initializes its member a_ with a copy of the argument a, the reference count 
of the pointer is incremented again (2 -> 3).
- After destruction of the constructor arguments, the reference count is decreased (3 -> 2).

This involves unnecessary copy operations.

## Example 2
```
A::A() {}
B::B(std::shared_ptr<A> a) : a_(std::move(a)) {}

C::C()
{
  a_ = std::make_shared<A>();
  b_ = std::make_unique<B>(a_);
}
```

- C passes a copy of a_ to B. The reference count of the pointer is incremented (1 -> 2).
- The constructor of B transfers the argument a into its member a_. The reference count is not incremented and the argument a becomes `nullptr`.
- Both C and B have a reference to the instance of A.

This is the best practice for passing in arguments where both the calling class and the called class need to have the pointer.

## Example 3
```
A::A() {}
B::B(std::shared_ptr<A> a) : a_(std::move(a)) {}

C::C()
{
  a = std::make_shared<A>();
  b_ = std::make_unique<B>(std::move(a));
}
```

- C directly passes the parameter a to B without copying. The reference count of the pointer is not incremented. a becomes `nullptr` and can't be used anymore in C.
- The constructor of B transfers the argument a into its member a_. The reference count is not incremented and the argument a becomes `nullptr`.
- Only B has a reference to the instance of A.

This is the best practice for passing in arguments where the calling class does not need the pointer anymore after passing it. Never apply on class members, as within the class the risk for accessing the members after passing it is high.

