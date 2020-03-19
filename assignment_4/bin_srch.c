#include <stdio.h>
#include <string.h>
#include <stdlib.h>


struct Node
{
	struct Node *node;
	struct Node *left;
	struct Node *right;
	struct Node *parent;
	char *elm;
	int	h; //height
	int printed; //flag used while printing
	//printed = 0;

};


/*
Node createNode(node)
{

	struct Node *node1;
	node1->parent = node;
	node1->left = NULL;
	node1->right = NULL;
	node1->elm = pch1[1];
	node1.h = node.h + 1;

	if (node->elm > pch1[1])
		{
			node->left = node1;
		}
	else if (node->elm < pch1[1])
		{
			node->right = node1;
		}


}
*/

/*
int main()
{

	char inp_str[] = "insert 567";
	char * inp_str_tokens;
	inp_str_tokens = strtok(inp_str," ");

	if(strcmp(inp_str_tokens[0],"insert",5))
		{
			printf("Hello World\n");
//			if(strcomp(inp_str_tokens[1],Node->value))

		}


	return 0;
}
*/
/* strtok example */

int main (int argc, char* argv[])
{

	printf("argc and argv are: %d and %s\n",argc,argv[1]);
	struct Node* root; //root node
 	char str[] ="insert 4353";
	printf("%s\n",str);
	//char pch[32];
	char* pch;

	pch = (char*)malloc(32 * sizeof(char));

	char* pch1[2];
	pch1[0] = (char*)malloc(50 * sizeof(char));
	pch1[1] = (char*)malloc(50 * sizeof(char));

 
	int i=0;
	int inserted = 0;
	int elem_counter = 0;
	FILE *fp;
	char* str1;
	char* line;
	line = (char*)malloc(50 * sizeof(char));


	fp = fopen(argv[1], "r");


	//fgets(str,100,stdin);
//	str1 = gets(fp);
//	printf("string is: %s\n",str1);

	struct Node* node = root; 
//	node->left = NULL;
//	node->right = NULL;


//	printf ("Splitting string \"%s\" into tokens:\n",str);
	pch = strtok (str," ");
//	printf("printing %s\n",pch);
	pch1[0] = pch;
	printf("aray elm is %s\n",pch1[0]);
	pch = strtok(NULL, " ");
//	printf("printing %s\n",pch);
	pch1[1] = pch;
	printf("aray elm is %s\n",pch1[1]);


/*
	while (pch != NULL)
	{
//			printf ("%s\n",pch);
		pch1[i] = pch;
		printf("array elm %s\n",pch1[i]);
		pch = strtok (NULL, " ");
		i++;

//    printf ("%s\n",pch);

	}
*/

//	printf("checking %s\n",pch1[0]);
//	printf("checking %s\n",pch1[1]);

	node->elm = &pch[1];
	node->left = NULL;
	node->right = NULL;
	node->parent = NULL; //i think this line is not required
	node->h = 0; //is it 0 or 1?
	elem_counter++;
	printf("just before while\n");

/*
	char line[32];
	while (!feof(fp))
	{
	    fgets(line, 32, fp);
	}
	printf("string is %s", line);
*/


	while (!feof(fp)) //correct this line
	{
		
		fgets(line, 32, fp);

		



		pch = strtok (line," ");
		while (pch != NULL)
		{
//			printf ("%s\n",pch);
			pch1[i] = pch;
//			printf("array elm %s\n",pch1[i]);
			pch = strtok (NULL, " ");
			i++;

//    printf ("%s\n",pch);

		}






		if (strcmp(pch1[0],"insert"))
		{
			while (inserted==0)
			{

				struct Node *node1;
//					node1->parent = node;
				node1->left = NULL;
				node1->right = NULL;
				node1->elm = pch1[1];
//					node1.h = node.h + 1;


/*
	if (node->elm > pch1[1])
		{
			node->left = node1;
		}
	else if (node->elm < pch1[1])
		{
			node->right = node1;
		}

*/
	
				if ((node->elm>pch1[1])&&(node->left == NULL))
				{
//							tree = createNode(node,pch1[1]);
					node->left = node1;
					node1->parent = node;
					node1->h = node->h + 1;
					inserted = 1;
					elem_counter++;
				}
				else if ((node->elm<pch1[1])&&(node->right == NULL))
				{
//							tree = createNode(node,pch1[1]);
					node->right = node1;
					node1->parent = node;
					node1->h = node->h + 1;
					inserted = 1;
					elem_counter++;
				}
				else if (node->elm > pch1[1])
				{
					node = node->left;
				}
				else if (node->elm < pch1[1])
				{
					node = node->right;
				}
				
			}

		}

		printf("just before break\n");
		break;
		
		if (strcmp(pch1[0],"print_pre"))
		{
			printf("%s\n",root->elm);
			root->printed = 1;
			elem_counter--;
			node = root;
			while(elem_counter!=0)
			{
				if((node->left!=NULL)&&(node->printed==1))
				{
					node = node->left;
					printf("%s\n",node->elm);
					node->printed = 1;
					elem_counter--;
				}
				else if((node->left==NULL)&&(node->right!=NULL)&&(node->printed==1))
				{
					node = node->right;
					printf("%s\n",node->elm);
					node->printed = 1;
					elem_counter--;
				}
				else if((node->left!=NULL)&&(node->right!=NULL)&&(node->printed==2))
				{
					node = node->right;
					printf("%s\n",node->elm);
					node->printed = 1;
					elem_counter--;
				}
				else if ((node->right==NULL)&&(node->printed==2))
				{
					node = node->parent;
					node->printed++;
				}
				else if ((node->printed==1)||(node->printed==2))//if ((node->left==NULL)&&(node->right==NULL))
				{
					node = node->parent;
					node->printed++;
				}
				else if (node->printed==3)
				{
					node = node->parent;
					node->printed++;
				}
				
			}
			

		}


		if (strcmp(pch1[0],"print_post"))
		{
//			printf("%s\n",root->elm);
//			root.printed = 1;
//			elem_counter--;
			node = root;
			while(elem_counter!=0)
			{
				if((node->left==NULL)&&(node->right==NULL)&&(node->printed ==0))//here printed means printed or passed
				{
					//node = node->left;
					printf("%s\n",node->elm);
					node->printed = 1;
					node = node->parent;
					elem_counter--;
				}
				else if((node->left!=NULL)&&(node->printed==0))//here printed flag means whether it has passed the node or not
				{
					node->printed = 1; //it means it has passed this node once
					node = node->left;
					//printf("%s\n",node->elm);
					//node.printed = 1;
				}
				else if ((node->left==NULL)&&(node->printed==0))
				{
					//printf("%s\n",node->elm);
					node->printed = 2; //it means it has been actually printed //anyway, this line is not required
					//node = node->parent;
				    node = node->right;
					//elem_counter--;
				}
				else if ((node->right!=NULL)&&(node->printed==1))
				{
					node->printed = 2; //it means it has passes this node twice
					node = node->right;
				}
				else if ((node->right==NULL)&&(node->printed==1))
				{
					printf("%s\n",node->elm);
					node->printed = 3; //it means it has been actually printed //anyway, this line is not required
					node = node->parent;
				    //node = node->right;
					elem_counter--;
				}
				else if (node->printed==2)
				{
					printf("%s\n",node->elm);
					node->printed = 3; //it means it has been actually printed //anyway, this line is not required
					node = node->parent;
				    //node = node->right;
					elem_counter--;
				}
			}
			printf("%s\n",node->elm);
			node->printed = 2; //not required
			

		}


//			node->left

	}

	fclose(fp);
	return 0;
}
