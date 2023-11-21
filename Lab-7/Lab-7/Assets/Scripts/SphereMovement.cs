using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class CubeMovement : MonoBehaviour
{
    public Rigidbody rb;

    // Start is called before the first frame update
    void Start()
    {
        rb = GetComponent<Rigidbody>();
    }

    // Update is called once per frame
    void Update()
    {
        if (Input.GetKeyDown(KeyCode.Space))
        {
            Debug.Log("Space key was pressed.");
            transform.Translate(Vector3.up);
        }

        if (Input.GetKey(KeyCode.UpArrow))
        {
            rb.AddForce(Vector3.forward, ForceMode.Force);
        }
        
    }
}
