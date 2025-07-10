const Gallery = ({images}) => {

    return (
        <div>
           { images && images.length > 0 ? (
            images.map((image, index) =>
                <li className="gallery" key={index}>
                    <img
                        className="gallery-screenshot"
                        src={image}
                        alt="undefined screenshot from query"
                        width='500'
                    />
                </li>
            )
           ) : (
            <div>
                <h3>You haven't made a screenshot yet!</h3>
            </div>
           )} 
        </div>
    )
}

export default Gallery;