# 0x12. JavaScript - Warm up

## Learning Objectives
- Why JavaScript programming is amazing
- How to run a JavaScript script
- How to create variables and constants

## Notes

### undefined
The __undefined__ global property represents the primitive value `undefined`.
It is one of JavaScript's primitive types. 

A variable that has not been assigned a value is of type `undefined`. A method
or statement also returns `undefined` if the variable that is being evaluated
does not have an assigned value. A function returns `undefined` if a value was
not _returned_.

You can use `undefined` and the strict equality and inequality operators to
determine whether a variable has a value.

```javascript
let x;

if (x === undefined) {
// these statements execute
} else {
// these statements do not execute
}
```
> The strict _equality_ operator must be used here, because it strictly
> compares two values for equality. Neither value is implicitly converted to
> some other value before being compared. If the values have different types,
> the values are considered unequal. if the values have the same types, the
> values are considered unequal. if the values have the same type, are not
> numbers, and have the same value, they're considered equal. [see more](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Equality_comparisons_and_sameness#strict_equality_using)
