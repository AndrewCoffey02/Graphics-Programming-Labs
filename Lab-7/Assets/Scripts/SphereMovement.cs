using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class CubeMovement : MonoBehaviour
{
    //rigidbody component
    public Rigidbody rb;

    // Start is called before the first frame update
    void Start()
    {
        //call the rigid component
        rb = GetComponent<Rigidbody>();
    }

    // Update is called once per frame
    void Update()
    {
        //make sphere jump vector
        if (Input.GetKeyDown(KeyCode.Space))
        {
            Debug.Log("Space key was pressed.");
            transform.Translate(Vector3.up);
        }

        //sphere movement across x ad z axis
        if (Input.GetKey(KeyCode.UpArrow))
        {
            rb.AddForce(Vector3.forward, ForceMode.Force);
        }
        if (Input.GetKey(KeyCode.DownArrow))
        {
            rb.AddForce(Vector3.back, ForceMode.Force);
        }
        if (Input.GetKey(KeyCode.LeftArrow))
        {
            rb.AddForce(Vector3.left, ForceMode.Force);
        }
        if (Input.GetKey(KeyCode.RightArrow))
        {
            rb.AddForce(Vector3.right, ForceMode.Force);
        }
        
    }
}
