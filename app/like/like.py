from main import FastAPI , Response , status , HTTPException, Depends, APIRouter
from main import Session
from app.like.models import Like
from app.database import engine , SessionLocal
from app.utils import pwd_context
from app.utils import get_db
from app import oauth2
from app.like.service import  get_all_likes_service , add_new_likes_service , get_via_id_service ,remove_like_service 

router= APIRouter(
    prefix="/like",
    tags= ['likes']
)

air = FastAPI()


@router.post("/add/{post_id}")
def like_post(
    post_id: int,
    db: Session = Depends(get_db),
    current_user = Depends(oauth2.get_current_user)
):

    existing_like = db.query(Like).filter(
        Like.post_id == post_id,
        Like.user_id == current_user.user_id
    ).first()

    if existing_like:
        raise HTTPException(status_code=400, detail="Already liked")

    new_like = Like(
        post_id=post_id,
        user_id=current_user.user_id
    )

    db.add(new_like)
    db.commit()

    return {"message": "Post liked"}




@router.delete("/remove/{post_id}")
def unlike_post(
    post_id: int,
    db: Session = Depends(get_db),
    current_user = Depends(oauth2.get_current_user)
):

    like = db.query(Like).filter(
        Like.post_id == post_id,
        Like.user_id == current_user.user_id
    )

    if not like.first():
        raise HTTPException(status_code=404, detail="Not liked")

    like.delete(synchronize_session=False)
    db.commit()

    return {"message": "Post unliked"}