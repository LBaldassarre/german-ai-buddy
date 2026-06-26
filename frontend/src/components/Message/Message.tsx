import "./Message.css";

type MessageProps = {
  writer: string;
  content: string;
};

function Message({writer, content}: MessageProps){

    function translation(content:string): string{
        // Need to do the API request here.
        return 'Translate API is still in the works!'
    }

    return(
        <>
            <div className={'cc-message ' + writer}>
                        <div className={"cc-message-"+ writer +"-content"}>{content}</div>
                        {writer === "buddy" && (
                            <div className="cc-message-buddy-translation">
                                {translation(content)}
                            </div>
                        )}
            </div>
        </>
    )
}

export default Message;