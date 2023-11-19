import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class SudokuSolverController {

    @PostMapping("/solve")
    public char[][] solveSudoku(@RequestBody char[][] board) {
        Solution solver = new Solution();
        solver.solveSudoku(board);
        return board;
    }
}
