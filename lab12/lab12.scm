(define-macro
 (if-macro condition if-true if-false)
 'YOUR-CODE-HERE
 `(if ,condition ,if-true,if-false)
)

(define-macro (or-macro expr1 expr2)
  `(let ((v1 ,expr1))
     (if v1
        v1
        ,expr2)))

(define (replicate x n) (if (zero? n) '() (cons x (replicate x (- n 1)))))

(define-macro (repeat-n expr n) 'YOUR-CODE-HERE (cons 'begin (replicate expr (eval n))))

(define
 (list-of map-expr for var in lst if filter-expr)
 'YOUR-CODE-HERE
   `(map (lambda (,var) ,map-expr)  (filter (lambda (,var),filter-expr) ,lst))
)

(define-macro (list-of-macro map-expr
                             for
                             var
                             in
                             lst
                             if
                             filter-expr)
  'YOUR-CODE-HERE
  `(map (lambda (,var) ,map-expr)  (filter (lambda (,var),filter-expr) ,lst))
)
