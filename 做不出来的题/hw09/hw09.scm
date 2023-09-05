(define-macro (when condition exprs)
  `(if ,condition ,(list 'begin exprs) 'okay) 
)

(define-macro (switch expr cases)
	(cons 'cond
		(map (lambda (case) (cons (list 'eq? expr (car case))(cdr case)))
    			cases))
)


