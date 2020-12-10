(defparameter +numbers+ (mapcar #'parse-integer (uiop:read-file-lines "input.txt")))

;; Solve for steps 1 and 2 using the same mechanism...
(macrolet ((find-numbers (l)
             `(block try-block
                (flet ((test-fn (p)
                         (when (equal 2020 (apply #'+ p))
                           (return-from try-block (apply #'* p)))))
                  (alexandria:map-combinations #'test-fn +numbers+ :length ,l)))))
  (print (find-numbers 2))
  (print (find-numbers 3)))






