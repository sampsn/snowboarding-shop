import json
from fastapi import FastAPI

from models import Brand, Board, BoardRequest


with open("snowboards.json", "r") as f:
    snowboard_list = json.load(f)

snowboards: list[Board] = [Board(**board) for board in snowboard_list]

app = FastAPI()


@app.get("/")
async def get_boards():
    return snowboards


@app.post("/")
async def create_board(board: BoardRequest) -> str:
    new_board = Board(
        id=snowboards[-1].id + 1,
        length=board.length,
        color=board.color,
        has_bindings=board.has_bindings,
        brand=board.brand,
    )
    snowboards.append(new_board)
    return "Board created successfully"


@app.put("/{board_id}")
async def update_board(board_id: int, board: BoardRequest) -> str:
    new_board = Board(
        id=board_id,
        length=board.length,
        color=board.color,
        has_bindings=board.has_bindings,
        brand=board.brand,
    )
    if board_id - 1 > len(snowboards):
        snowboards.append(new_board)
    else:
        snowboards[board_id - 1] = new_board
    return "Board updated successfully"


@app.delete("/{board_id}")
async def delete_board(board_id: int) -> str:
    for snowboard in snowboards:
        if snowboard.id == board_id:
            snowboards.remove(snowboard)

    return "Board deleted successfully"
