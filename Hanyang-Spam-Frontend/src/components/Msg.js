import React from "react";

const Msg = ({when,p_num,id,filter,msg}) => {
  return (
    <div className="msg">
      <div className="message">{msg}</div>
      <div>
        <span className="p_num">{p_num}</span>
        <span className="when">{when}</span>
      </div>
      
    </div>
  );
};

export default Msg;
