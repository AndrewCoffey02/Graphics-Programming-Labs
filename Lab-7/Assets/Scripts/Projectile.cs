using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using Unity.VisualScripting;

public class Projectile : MonoBehaviour
{
    public GameObject Cube;
    float vel = -2;
    // Start is called before the first frame update
    void Start()
    {
        
    }

    // Update is called once per frame
    void Update()
    {
        if(Input.GetKeyDown(KeyCode.Space)){

            Instantiate(Cube, new Vector3(vel, 1, 0), Quaternion.identity);
            
        }
    }
}

