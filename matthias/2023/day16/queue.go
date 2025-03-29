package main

type MemQueue[T comparable] struct {
	elements []T
	cache    map[T]bool
}

func NewQ[T comparable]() *MemQueue[T] {
	return &MemQueue[T]{
		elements: []T{},
		cache:    map[T]bool{},
	}
}

func (q *MemQueue[T]) Push(e T) {
	if !q.cache[e] {
		q.cache[e] = true
		q.elements = append(q.elements, e)
	}
}

func (q *MemQueue[T]) Pop() (e T) {
	if len(q.elements) == 0 {
		var t T
		return t
	}
	e = q.elements[0]
	q.elements = q.elements[1:]
	return e
}

func (q *MemQueue[T]) Empty() bool {
	return len(q.elements) == 0
}

func (q *MemQueue[T]) CacheLength() int {
	return len(q.cache)
}

func (q *MemQueue[T]) CacheElements() []T {
	result := make([]T, len(q.cache))
	i := 0
	for t := range q.cache {
		result[i] = t
		i++
	}
	return result
}
